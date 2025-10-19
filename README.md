# 🗳️ Sistema de Urna Eletrônica para o Grêmio Estudantil  
**Escola Rogério Lázaro Toccheton**  

## 📚 Contexto e Motivação  
O **grêmio estudantil** é uma entidade que representa os alunos e promove a participação ativa nas decisões da escola, na organização de eventos e na melhoria da gestão escolar.  

Na **Escola Rogério Lázaro Toccheton**, as eleições para o grêmio eram realizadas por meio de formulários online, o que apresentava algumas limitações, como **possibilidade de votos duplicados** e **falta de controle sobre a autenticidade dos eleitores**.  

Diante desse cenário, os alunos **Marcos Andrei de Souza Almeida**, **Victor Alexandre de Carvalho Pedroza** e **Guilherme da Silva Barreto** desenvolveram um **sistema de urna eletrônica** com o objetivo de tornar o processo mais **seguro, justo e transparente**, garantindo que cada aluno pudesse votar **apenas uma vez** e com **maior proteção das informações**.  

O projeto foi finalizado e **aprovado para uso oficial nas eleições do grêmio de 2024**.

---

## ⚙️ Funcionamento do Sistema  

### 🔐 Tela de Login  
- O sistema solicita o **RA (Registro do Aluno)** como credencial de acesso.  
- Apenas RAs válidos — com **formato padronizado (três zeros à frente)** e **registrados no banco de dados** — permitem o acesso à etapa de votação.  

### 🗳️ Validação de Voto  
- Após a autenticação, o aluno é direcionado para a **tela de votação**.  
- O sistema **bloqueia automaticamente o RA** após o voto, impedindo múltiplas votações com o mesmo registro.  

### 🔑 Acesso Administrativo  
- Foi implementada uma **palavra-chave administrativa secreta (`__MGV__`)**, que permite o acesso restrito à equipe gestora da escola em caso de revisão ou correção técnica.  

### ✅ Finalização e Créditos  
- Após o voto, o sistema exibe uma mensagem de confirmação e apresenta os **créditos dos desenvolvedores**.  
- Tentativas de novo acesso são bloqueadas, **garantindo a integridade e transparência** do processo eleitoral.  

---

## 🗂️ Banco de Dados  
Para preservar a **segurança e a privacidade dos alunos**, todas as informações utilizadas no banco de dados foram **substituídas por dados fictícios gerados por IA**, evitando qualquer exposição de dados reais.  

---

## 🧠 Tecnologias Utilizadas  
- **Python** → Linguagem principal utilizada no desenvolvimento do sistema.  
- **SQLite** → Banco de dados leve e eficiente para armazenamento local de alunos e votos.  
- **DB Browser for SQLite** → Ferramenta utilizada para criação, visualização e gerenciamento do banco de dados.  

---

## 🏁 Resultados e Conclusão  
O projeto foi **concluído no início de 2024** e aprovado pela **direção escolar** para uso nas eleições do grêmio estudantil.  
Durante o processo eleitoral, o sistema operou de forma **estável e confiável**, proporcionando **maior transparência, segurança e organização** à votação.  

---

## 👨‍💻 Equipe de Desenvolvimento  
- **Marcos Andrei de Souza Almeida**  
- **Victor Alexandre de Carvalho Pedroza**  
- **Guilherme da Silva Barreto**  
