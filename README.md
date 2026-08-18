# PetAdote

Sistema Django para consulta de animais, acompanhamento de saúde e vacinação e
gerenciamento de solicitações de adoção.

## Como criar o ZIP para compartilhar

Não compacte apenas os arquivos mostrados pelo GitHub: o banco de dados e as
imagens enviadas pelos usuários não são versionados. Na raiz do projeto, execute:

```bash
python criar_pacote.py
```

O arquivo será criado em `dist/PetAdote-compartilhamento.zip`. Esse pacote inclui
`db.sqlite3` e `media/`, preservando os dados e as fotos de teste. Ele não inclui
o histórico do Git, ambientes virtuais, caches nem arquivos gerados pelo Django.

> Atenção: o banco incluído no ZIP contém os usuários e demais dados cadastrados
> localmente. Compartilhe o pacote somente com pessoas autorizadas.

## Como executar em outro computador

É necessário ter o Python instalado. Depois de extrair o ZIP, abra o terminal na
pasta `PetAdote` e crie um ambiente virtual.

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

Se o PowerShell impedir a ativação do ambiente, os comandos também podem ser
executados diretamente:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

### Linux ou macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abra `http://127.0.0.1:8000/` no navegador. Não abra os arquivos HTML
diretamente, pois eles são templates e precisam ser processados pelo Django.

## Conteúdo que precisa acompanhar o projeto

- `db.sqlite3`: dados e contas cadastradas;
- `media/`: fotos dos animais e dos perfis;
- pastas `static/` dos aplicativos: CSS e imagens fixas do site;
- `requirements.txt`: versões das dependências Python;
- migrações dos aplicativos.

Para criar um banco vazio em vez de usar os dados de demonstração, remova o
`db.sqlite3` depois de extrair o pacote e execute `python manage.py migrate`.
