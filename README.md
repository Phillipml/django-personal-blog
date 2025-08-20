# Django Personal Blog

Um blog pessoal desenvolvido com Django, framework web Python moderno e robusto.

## 🚀 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **Editor de código** (VS Code, PyCharm, Sublime Text, etc.)

## 📋 Instalação e Configuração

### 1. **Clonar o Repositório**

```bash
git clone <url-do-repositorio>
cd django-personal-blog
```

### 2. **Navegar para o Diretório do Projeto**

```bash
# IMPORTANTE: Fique na raiz do projeto (onde está o README.md)
# NÃO entre na pasta personal_blog ainda
```

### 3. **Criar Ambiente Virtual**

É altamente recomendado usar um ambiente virtual para isolar as dependências:

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
.\venv\Scripts\activate
# OU para Linux/Mac
source venv/bin/activate
```

**Dica:** Você saberá que o ambiente virtual está ativo quando ver `(venv)` no início da linha do terminal.

### 4. **Instalar Dependências**

Com o ambiente virtual ativado, instale o Django:

```bash
pip install django
```

### 5. **Navegar para o Diretório Django**

```bash
cd personal_blog
```

### 6. **Verificar Instalação**

Confirme que o Django foi instalado corretamente:

```bash
python manage.py --version
```

## 🗄️ Configuração do Banco de Dados

### 7. **Executar Migrações**

Configure o banco de dados inicial:

```bash
# Criar arquivos de migração
python manage.py makemigrations

# Aplicar migrações ao banco
python manage.py migrate
```

### 8. **Criar Superusuário (Opcional)**

Para acessar o painel administrativo do Django:

```bash
python manage.py createsuperuser
```

Siga as instruções para criar um usuário e senha.

## 🚀 Executando o Projeto

### 9. **Iniciar Servidor de Desenvolvimento**

```bash
python manage.py runserver
```

### 10. **Acessar o Projeto**

- **Site principal:** http://127.0.0.1:8000/
- **Painel administrativo:** http://127.0.0.1:8000/admin/

## 📁 Estrutura do Projeto

```
django-personal-blog/           ← Raiz do projeto
├── venv/                      ← Ambiente virtual (criar aqui)
├── personal_blog/             ← Projeto Django
│   ├── manage.py
│   ├── personal_blog/         # Configurações principais
│   │   ├── __init__.py
│   │   ├── settings.py        # Configurações do Django
│   │   ├── urls.py           # URLs principais
│   │   ├── wsgi.py           # Configuração WSGI
│   │   └── asgi.py           # Configuração ASGI
│   └── blog/                  # Aplicação principal do blog
│       ├── __init__.py
│       ├── admin.py          # Configuração do painel admin
│       ├── apps.py           # Configuração da aplicação
│       ├── models/           # Modelos de dados
│       ├── views.py          # Lógica de visualização
│       ├── tests.py          # Testes automatizados
│       └── migrations/       # Arquivos de migração do banco
├── manage.py                 # Script de gerenciamento do Django
├── README.md                 # Este arquivo
└── .gitignore               # Arquivos ignorados pelo Git
```

## 🛠️ Comandos Úteis

### Desenvolvimento

```bash
# Executar testes
python manage.py test

# Criar nova migração após alterar modelos
python manage.py makemigrations

# Aplicar migrações pendentes
python manage.py migrate

# Acessar shell interativo do Django
python manage.py shell

# Coletar arquivos estáticos (produção)
python manage.py collectstatic
```

### Gerenciamento de Usuários

```bash
# Criar novo usuário
python manage.py createsuperuser

# Alterar senha de usuário
python manage.py changepassword <username>
```

## 🔧 Configurações Importantes

### Arquivo `settings.py`

- **DEBUG = True** - Modo de desenvolvimento (desative em produção)
- **SECRET_KEY** - Chave secreta para segurança (não compartilhe)
- **DATABASES** - Configurado para SQLite por padrão
- **INSTALLED_APPS** - Inclui o app `blog` e apps padrão do Django

### Banco de Dados

Por padrão, o projeto usa **SQLite3**, que é perfeito para desenvolvimento. Para produção, considere usar PostgreSQL ou MySQL.

## 🚨 Solução de Problemas Comuns

### Erro: "No module named 'django'"

- **Solução:** Ative o ambiente virtual: `.\venv\Scripts\Activate.ps1`

### Erro: "Port already in use"

- **Solução:** Use uma porta diferente: `python manage.py runserver 8001`

### Erro: "Database is locked"

- **Solução:** Feche outros processos que possam estar usando o banco

## 📚 Próximos Passos

Após iniciar o projeto com sucesso:

1. **Personalizar o Blog:**

   - Editar `blog/views.py` para criar suas próprias views
   - Modificar `personal_blog/urls.py` para configurar rotas
   - Criar templates HTML em `blog/templates/`

2. **Adicionar Funcionalidades:**

   - Sistema de comentários
   - Categorias de posts
   - Sistema de tags
   - Upload de imagens

3. **Melhorar o Design:**
   - Adicionar CSS personalizado
   - Implementar design responsivo
   - Integrar com frameworks CSS (Bootstrap, Tailwind)

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença especificada no arquivo `LICENSE`.

## 🆘 Suporte

Se encontrar problemas ou tiver dúvidas:

1. Verifique se seguiu todos os passos corretamente
2. Consulte a [documentação oficial do Django](https://docs.djangoproject.com/)
3. Abra uma issue no repositório

---

**Happy Coding! 🎉**
