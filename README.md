# Artigo Hub

**Artigo Hub** é um sistema simples de gerenciamento de artigos, onde os usuários podem criar, editar, excluir e comentar artigos. O projeto utiliza o Django como framework backend, e oferece um sistema de autenticação para usuários, permitindo que apenas os usuários logados possam criar e interagir com os artigos.

## Funcionalidades

- **Autenticação de Usuários**: Registro, login e logout de usuários.
- **Gerenciamento de Artigos**: Criação, edição e exclusão de artigos.
- **Comentários**: Os usuários podem comentar nos artigos.
- **Visualização de Artigos**: Exibição de uma lista de artigos e visualização de detalhes de cada artigo.
  
## Tecnologias

- **Django** (Framework backend)
- **SQLite** (Banco de dados, por padrão)
- **Bootstrap** (Frontend básico)

## Pré-requisitos

Antes de rodar o projeto, verifique se você tem as seguintes ferramentas instaladas:

- **Python** (versão 3.x)
- **Pip** (gerenciador de pacotes do Python)

## Instalação

1. **Clone o repositório** para sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/artigo-hub.git
   cd artigo-hub
   ```

2. **Crie um ambiente virtual** (se não tiver um já configurado):

   ```bash
   python -m venv .venv
   ```

3. **Ative o ambiente virtual**:

   - **No Windows**:

     ```bash
     .venv\Scripts\activate
     ```

   - **No macOS/Linux**:

     ```bash
     source .venv/bin/activate
     ```

4. **Instale as dependências** do projeto:

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure o banco de dados** (criação de tabelas e migrações):

   ```bash
   python manage.py migrate
   ```

6. **Crie um superusuário** para poder acessar o painel de administração do Django:

   ```bash
   python manage.py createsuperuser
   ```

   Você será solicitado a fornecer um nome de usuário, e-mail e senha.

7. **Execute o servidor de desenvolvimento**:

   ```bash
   python manage.py runserver
   ```

8. Agora, você pode acessar o projeto no navegador em: `http://127.0.0.1:8000/`.

## Como Usar

- Acesse o painel de administração com o superusuário que você criou em: `http://127.0.0.1:8000/admin/`.
- O sistema permite criar, editar e excluir artigos. 
- Usuários registrados podem comentar nos artigos.
  
## Contribuição

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/artigo-hub.git
   ```

2. **Crie uma branch para suas mudanças**:

   ```bash
   git checkout -b minha-nova-feature
   ```

3. **Faça suas mudanças e commit**:

   ```bash
   git add .
   git commit -m "Descrição do que foi feito"
   ```

4. **Envie suas mudanças para o repositório**:

   ```bash
   git push origin minha-nova-feature
   ```

5. **Abra um pull request** para o repositório original.
