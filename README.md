# 🚀 GlucoTrack

**GlucoTrack** é uma aplicação para controle de diabetes, facilitando o acompanhamento dos níveis de glicemia e do consumo de calorias de forma simples e eficiente.

## 📋 Descrição

Este projeto foi desenvolvido como parte da disciplina de **Projetos** na **Cesar School**, pela **Equipe 3**.

### 👥 Equipe

- **Lucas Carvalho**: 👨‍💼 Gerente de Projeto  
- **João Rietra**: 👨‍💻 Líder Técnico  
- **Lucas Lima**: 👨‍💻 Desenvolvedor  
- **Ivo Caetano**: 👨‍💻 Desenvolvedor  

## 🛠️ Arquitetura do Projeto

O GlucoTrack segue o padrão de arquitetura **MVC (Model-View-Controller)**, permitindo a separação entre as camadas de:

- **Regra de negócio** (Controller)
- **Modelo de dados** (Model)
- **Interface com o usuário** (View)

Essa abordagem facilita a organização do desenvolvimento, a divisão de tarefas e a manutenção do código.

### 🔍 Camadas do Projeto

- **Model (Dados)**: 📂 Atualmente, os dados são armazenados em arquivos JSON.
- **View (Interface com o Usuário)**: 🖥️ A interface com o usuário, no momento, é baseada em console.
- **Controller (Regras de Negócio)**: ⚙️ Controla a interação entre Model e View, garantindo o funcionamento adequado do sistema.

No futuro, planejamos expandir e desacoplar as camadas, permitindo integração com novas tecnologias, como bancos de dados relacionais, NoSQL, serviços em nuvem e interfaces gráficas mais intuitivas.

## 📦 Dependências

Para rodar o **GlucoTrack**, você precisará das seguintes bibliotecas Python:

- **PrettyTable**: 📊 Para exibir dados em formato de tabela no console.
- **PyFiglet**: 🎨 Para exibir títulos estilizados no console.

### 📥 Instruções de Instalação

Execute os comandos abaixo para instalar as dependências:

```bash
pip install prettytable
pip install pyfiglet
