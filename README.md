GlucoTrack

Aplicação para controle de diabetes fazendo o acompanhamento da glicemia e do consumo de calorias.

Projeto da cadeira de Projetos da Cesar School.

Equipe 3

Lucas Carvalho: Gerente de Projeto;
João Rietra: Líder Técnico;
Lucas Lima: Desenvolvedor;
Ivo Caetano: Desenvolvedor;

A aplicação está organizada no modelo MVC por permitir a separação em camadas de regras de negócio, modelo de dados e interface com o usuário,
permitindo que a equipe possa se dividir no desenvolvimento da aplicação e facilitar a manutenção.

Neste momento, a camada de dados está baseada em arquivos no formato json. A camada de interface com o usuário utiliza o console.
No futuro, através de interfaces, implementaremos mais desacoplamento permitindo que cada camada possa utilizar tecnologias diferentes (bancos de dados relacionais,
NOSQL, serviços em nuvem, interface com usuário mais robustas e visuais, etc).

Para rodar é necessário instalar no python as bibliotecas:
PrettyTable: para exibição de dados em tabelas no console
PyFiglet: para exibição de títulos amigáveis no console

Instruções para instalação das bibliotecas:
pip install prettytable
pip install pyfiglet
