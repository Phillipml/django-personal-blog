# Django Personal Blog

Um blog pessoal completo desenvolvido com Django, demonstrando as melhores práticas do framework Python para desenvolvimento web.

# 📸 Screenshot da Aplicação

![Screenshot da Aplicação](https://raw.githubusercontent.com/Phillipml/django-personal-blog/main/public/screenshot.png)
_Interface do blog Django com listagem de posts e design responsivo_

# ✨ Funcionalidades

## Sistema de Posts:
Criação, edição e publicação de artigos
## Painel Administrativo:
Interface completa para gerenciar conteúdo
## Design Responsivo:
Interface adaptável com Bootstrap
## Sistema de Usuários:
Autenticação e autorização integradas
## URLs Amigáveis:
Sistema de slugs para URLs limpas
## Testes Automatizados:
Cobertura de testes com pytest
## Templates Dinâmicos:
Sistema de templates Django com herança

# 🛠️ Tecnologias Utilizadas

## Django 5.2.5:
Framework web Python
## Python 3.8+:
Linguagem de programação
## SQLite3:
Banco de dados (desenvolvimento)
## Bootstrap 4:
Framework CSS
## pytest:
Framework de testes
## Factory Boy:
Geração de dados para testes
## Faker:
Dados fictícios para desenvolvimento

# 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório:**

```bash
git clone <url-do-repositorio>
cd django-personal-blog
```

2. **Crie e ative o ambiente virtual:**

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Configure o banco de dados:**

```bash
cd personal_blog
python manage.py migrate
```

5. **Crie um superusuário (opcional):**

```bash
python manage.py createsuperuser
```

6. **Execute o servidor:**

```bash
python manage.py runserver
```

7. **Acesse a aplicação:**

- **Blog:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/

# 📁 Estrutura do Projeto

```
django-personal-blog/
├── personal_blog/              # Projeto Django principal
│   ├── blog/                  # Aplicação do blog
│   │   ├── models/            # Modelos de dados
│   │   ├── views/             # Views e lógica de negócio
│   │   ├── admin.py           # Configuração do painel admin
│   │   └── migrations/        # Migrações do banco
│   ├── templates/             # Templates HTML
│   ├── personal_blog/         # Configurações do projeto
│   └── manage.py              # Script de gerenciamento
├── tests/                     # Testes automatizados
├── public/                    # Screenshots e assets
├── requirements.txt           # Dependências do projeto
└── pytest.ini               # Configuração do pytest
```

# 🧪 Testes

Execute os testes com pytest:

```bash
# Executar todos os testes
pytest

# Executar testes com cobertura
pytest --cov=blog

# Executar testes específicos
pytest tests/models/
```

# 🎯 Características Técnicas

- **Arquitetura MVC**: Separação clara entre modelos, views e templates
- **ORM Django**: Mapeamento objeto-relacional para interação com banco
- **Sistema de Migrações**: Controle de versão do esquema do banco
- **Class-Based Views**: Views baseadas em classes para reutilização
- **Template Inheritance**: Sistema de herança de templates
- **Admin Interface**: Painel administrativo automático e customizável
- **Testes Unitários**: Cobertura completa com pytest e Factory Boy

# 📝 Uso

1. **Criar Posts**: Acesse o painel admin para criar novos posts
2. **Gerenciar Conteúdo**: Use a interface administrativa para editar posts
3. **Visualizar Blog**: Navegue pela interface pública para ler os posts
4. **Personalizar**: Modifique templates e estilos conforme necessário

# 🔧 Comandos Úteis

```bash
# Criar nova migração
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Executar testes
python manage.py test

# Shell interativo
python manage.py shell

# Coletar arquivos estáticos
python manage.py collectstatic
```

# 📄 Licença

Este projeto está sob a licença especificada no arquivo `LICENSE`.

---

**Desenvolvido por:**
Phillip Menezes

**Email:**
contato.phillip.menezes@gmail.com  
**LinkedIn:**
[Phillip Menezes](https://www.linkedin.com/in/phillip-menezes-063a39227/)  
**GitHub:**
[Phillipml](https://github.com/Phillipml/)
