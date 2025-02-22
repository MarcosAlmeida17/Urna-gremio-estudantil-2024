import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
import pygame
import pandas as pd
import sqlite3

janela = ctk.CTk()

conexao = sqlite3.connect('VotosDoGremio.db')

cursor = conexao.cursor()

def tela_voto():

    tabela = pd.read_sql('SELECT * FROM votos', conexao)
    
    lista_alunos = [aluno for aluno in tabela['RA']]
        
    df_ra = pd.read_sql('select * from ra_alunos', conexao)
    df_ra['RA_Aluno'] = '000' + df_ra['RA'] + df_ra['Dig. RA']
    
    lista_ra = ['__MGV__']
    
    for aluno in df_ra['RA_Aluno']:
        lista_ra.append(aluno)
        
    if ra_entry.get() in lista_alunos and not ra_entry.get() == '__MGV__':
        messagebox.showerror(title='Erro', message='Você já votou utilizando esse RA')

    elif not ra_entry.get() in lista_ra:
        messagebox.showerror(title='Erro', message='Confirme se o RA está preenchido corretamente')

    else:

        global frame_voto
        
        # Tela de voto

        frame_login.place(x=0, y=10000)
        frame_voto = ctk.CTkFrame(janela, width=500, height=330)
        frame_voto.place(x=150, y=100)

        label_voto = ctk.CTkLabel(frame_voto, text='Escolha o grêmio de sua preferência', font=('Berlin Sans FB Demi', 25))
        label_voto.place(x=52, y=40)
        
        global gremios, cb_gremios, texto
        
        df_gremios = pd.read_sql('select * from gremios', conexao)

        gremios = []
        
        for gremio in df_gremios['Gremio']:
            gremios.append(gremio)

        cb_gremios = ctk.CTkOptionMenu(frame_voto, values=gremios, width=300, height=44, text_color='white')
        cb_gremios.place(x=103, y=120)
        
        global ra

        ra = ra_entry.get()
        
        button_enviar2 = ctk.CTkButton(frame_voto, text='Enviar', width=176, height=50, font=('Berlin Sans FB Demi', 20),
                                       command=computar_info)
        button_enviar2.place(x=158, y=215)

def computar_info():
    
    resposta = messagebox.askyesno("Confirmação", "Você tem certeza da sua escolha?")
    
    if resposta == True:
        pygame.init()
        pygame.mixer.music.load('SOM DE BOTÃO VIRTUAL.mp3')
        pygame.mixer.music.play()

        frame_voto.place(x=0, y=1000)
        voto = cb_gremios.get()

        cursor.execute(f"""INSERT INTO votos ('RA', 'Voto')
        VALUES ('{ra}', '{voto}')
        """)

        conexao.commit()

        global frame_final

        # tela final

        frame_final = ctk.CTkFrame(janela, width=500, height=330)
        frame_final.place(x=150, y=100)

        label_final = ctk.CTkLabel(frame_final, text='VOTO COMPUTADO COM SUCESSO', font=('Berlin Sans FB Demi', 25))
        label_final.place(x=54, y=30)

        button_voltar = ctk.CTkButton(frame_final, text='Voltar para o início', font=('Berlin Sans FB Demi', 20),
                                     width=100, height=50, command=voltar_inicio)
        button_voltar.place(x=158, y=85)

        creditos = ctk.CTkLabel(frame_final, text='''Feito por:
@Marcos.a897
@Guizin.fut7
@Virto.021
''', width=220, height=80, font=('Berlin Sans FB Demi', 25), text_color='#ED0E2B')
        creditos.place(x=139, y=160)
    
def voltar_inicio():
    frame_login.place(x=150, y=100)
    frame_final.place(x=160, y=1100)
    ra_entry.delete(0, 'end')

# Tela inicial

janela.geometry('800x500')

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')

janela.title('Urna Elêtronica')

janela.resizable(False, False)

janela.iconbitmap('noun_14292-1.ico')


img = ctk.CTkImage(Image.open('urna_gremio.png'), size=(800, 500))
label_img = ctk.CTkLabel(janela, image=img, text='')
label_img.place(x=0, y=0)

frame_login = ctk.CTkFrame(janela, width=500, height=330)
frame_login.place(x=150, y=100)

label_login = ctk.CTkLabel(frame_login, text='INFORME O SEU RA', font=('Berlin Sans FB Demi', 20))
label_login.place(x=167, y=68)

ra_entry = ctk.CTkEntry(frame_login, placeholder_text='Insira seu RA', width=220, height=45, text_color='green')
ra_entry.place(x=144, y=120)


button_enviar = ctk.CTkButton(frame_login, text='Enviar', width=176, height=50, font=('Berlin Sans FB Demi', 20),
                              command=tela_voto)
button_enviar.place(x=165, y=190)

janela.mainloop()


cursor.close()
conexao.close()




