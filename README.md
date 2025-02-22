# Projeto urna para grêmio estudantil escola Rógerio Lázaro Toccheton.

### Contexto e Motivação:

O grêmio estudantil é uma organização que representa os alunos, permitindo que participem de decisões da escola,
organizem eventos e auxiliem na gestão escolar. Na Escola Rogério Lázaro Toccheton,
as eleições para o grêmio eram realizadas através de formulários online, mas com algumas limitações,
como a possibilidade de votos duplicados e falta de controle rigoroso.Diante disso, os alunos __Marcos Andrei de Souza Almeida__,
__Victor Alexandre de Carvalho Pedroza__ e __Guilherme da Silva Barreto__ decidiram criar um software mais seguro e eficiente para garantir
uma votação justa,onde cada aluno pudesse votar apenas uma vez e com maior proteção das informações.
O projeto foi desenvolvido para modernizar o processo eleitoral e foi aprovado para uso nas eleições de 2024.

### Funcionamento do Software:
 - Tela de Login: O sistema solicita o RA (Registro do Aluno) na tela inicial.
O aluno só consegue acessar a próxima etapa se o RA for válido precisando ter sempre 3 zeros na frente e estiver registrado no banco de dados.
 - Validação de Voto: Caso o RA esteja no banco de dados, o aluno é direcionado à tela de votação.
Para garantir que ninguém vote mais de uma vez, o sistema bloqueia o RA após o voto, permitindo apenas uma votação por aluno.
 - Palavra-Chave para Administração: Para assegurar que membros da direção possam ter acesso mesmo em caso de erro ou necessidade de revisão,
foi implementada uma palavra-chave secreta (`__MGV__`) que permite a entrada de administradores ao sistema.
 - Finalização e Créditos: Após o voto, o software mostra os créditos com os nomes de todos os envolvidos no projeto e confirma a votação.
Se o aluno tentar votar novamente, o sistema impede a entrada, garantindo a integridade do processo.

### Banco de Dados:
  Para garantir a segurança e a privacidade dos dados dos alunos,
todos os dados no banco foram substituídos por informações fictícias criadas por IA.
Isso evitou a exposição de dados reais, mantendo a confidencialidade.

### Tecnologias Utilizadas:
 - Python: A linguagem principal utilizada para desenvolver o sistema de backend.
 - SQLite: Utilizado para armazenar os dados de alunos e votos, garantindo que os registros sejam acessados de forma eficiente.
 - DB Browser: Ferramenta utilizada para criar e gerenciar o banco de dados.

### Conclusão:
  O projeto foi concluído no início de 2024 e foi aprovado pela direção da escola para ser utilizado nas eleições do grêmio estudantil.
Durante a votação, o sistema funcionou sem problemas técnicos e foi considerado eficiente,
ajudando a melhorar a organização e transparência do processo eleitoral.

### Equipe do Projeto:
- Marcos Andrei de Souza Almeida
- Victor Alexandre de Carvalho Pedroza
- Guilherme da Silva Barreto
