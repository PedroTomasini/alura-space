# Galeria de Fotos - Alura Space

Este é um projeto de galeria de fotos desenvolvido com Django. Ele permite que os usuários se cadastrem, façam login e gerenciem suas próprias fotos, com opções de adicionar, visualizar, editar e excluir fotografias.

## Funcionalidades

- **Cadastro de Usuário**: Permite que novos usuários se registrem no sistema.
- **Login e Logout**: Os usuários podem fazer login para acessar suas funcionalidades e sair quando desejarem.
- **CRUD de Fotografias**: 
  - **Criar**: Após logar, os usuários podem adicionar novas fotografias com título, descrição e legenda.
  - **Visualizar**: Os usuários podem visualizar as fotografias adicionadas em uma galeria.
  - **Editar**: Os usuários podem editar informações de suas fotografias.
  - **Excluir**: Os usuários podem remover suas fotografias da galeria.

## Tecnologias Utilizadas

- Python 3.12
- Django 5.1
- Banco de dados (SQLite, PostgreSQL, etc.)
- AWS S3 (para armazenar arquivos estáticos, se aplicável)
  
## Configuração do Ambiente

### Pré-requisitos

- Python 3.12 ou superior
- Django 5.1 ou superior
- Dependências adicionais estão listadas no arquivo `requirements.txt`

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/PedroTomasini/alura-space.git
   cd alura-space
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Em Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente no `.env`:
   ```bash
   SECRET_KEY=suachavesecreta
   AWS_ACCESS_KEY_ID=sua-chave-de-acesso
   AWS_SECRET_ACCESS_KEY=sua-chave-secreta
   AWS_STORAGE_BUCKET_NAME=seu-bucket-s3
   ```

5. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

6. Coleta de arquivos estáticos (para produção):
   ```bash
   python manage.py collectstatic
   ```

7. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

### Configuração de Armazenamento S3 (Opcional)

Se você deseja armazenar arquivos estáticos e mídia no S3, certifique-se de configurar o `django-storages` e definir as variáveis de ambiente `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_STORAGE_BUCKET_NAME`, e `AWS_S3_CUSTOM_DOMAIN`.

## Uso

1. Acesse a página inicial do sistema no navegador em `http://127.0.0.1:8000/`.
2. Cadastre-se ou faça login para acessar a galeria.
3. Após o login, utilize a interface para adicionar fotografias, especificando o título, descrição e legenda.
4. Navegue pela galeria para visualizar suas fotos, ou utilize as opções de editar e excluir.

## Estrutura do Projeto

- **`accounts`**: Contém a configuração de autenticação e funcionalidades de login, cadastro e logout.
- **`galeria`**: Aplicação principal que gerencia o CRUD de fotografias.
- **`static`**: Arquivos estáticos (CSS, JS) do projeto.
- **`templates`**: Arquivos HTML para as páginas do projeto.

## Contribuição

1. Faça um fork do projeto
2. Crie uma nova branch para sua feature (`git checkout -b feature/nova-feature`)
3. Faça o commit das suas alterações (`git commit -m 'Adicionei uma nova feature'`)
4. Faça o push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
