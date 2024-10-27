# AWS Credentials Clipboard Updater

O AWS Credentials Clipboard Updater é um utilitário de linha de comando (CLI) para gerenciar as credenciais da AWS. Ele permite atualizar, listar ou deletar perfis no seu arquivo de credenciais AWS de maneira prática e intuitiva

## Instalação

### Pré-requisitos
Certifique-se de que você tem o Python 3.7 ou superior instalado no seu sistema. Recomendamos o uso de ambientes virtuais para isolar as dependências do projeto. Se você estiver usando ferramentas como `virtualenv`, `pyenv-virtualenv` ou `venv`, siga as instruções abaixo.

### Passo a passo para instalação

#### 1. Clone o repositório do projeto:
```shell
git clone https://github.com/vavasilva/aws-credentials-clipboard-updater.git
```

#### 2. Navegue até o diretório do projeto:
```shell
cd aws-credentials-clipboard-updater
```

#### 3. Crie um ambiente virtual (opcional, mas recomendado):
Se você deseja utilizar um ambiente virtual para gerenciar as dependências do projeto, siga estas instruções:

##### Utilizando `virtualenv`:
```shell
python -m venv venv
source venv/bin/activate
```

##### Utilizando `pyenv` com `pyenv-virtualenv`:
```shell
pyenv virtualenv 3.12.0 aws-credentials-clipboard-updater
pyenv activate aws-credentials-clipboard-updater
```

#### 4. Instale as dependências:
Após ativar o ambiente virtual (se aplicável), instale as dependências listadas no arquivo `requirements.txt`:

```shell
pip install -r requirements.txt
```

#### 5. Instale o projeto em modo editável:
Instale o projeto no modo editável para que o comando `awscreds` seja reconhecido globalmente dentro do ambiente virtual:

```shell
pip install --editable .
```

> **Nota**: Se você não estiver usando um ambiente virtual, pode ser necessário usar `pip install --user --editable .` para evitar permissões de sistema.

### Dependências para Clipboard

Para garantir que as dependências específicas para manipulação de clipboard funcionem corretamente, você pode precisar instalar pacotes adicionais de acordo com o seu sistema operacional:

- **Arch Linux**:
  ```shell
  sudo pacman -S xclip xsel
  ```
  
- **Debian/Ubuntu**:
  ```shell
  sudo apt-get install xclip xsel
  ```

- **Red Hat/Fedora**:
  ```shell
  sudo dnf install xclip xsel
  ```

## Uso

Depois de configurar o ambiente e instalar as dependências, você pode usar o utilitário `awscreds` para gerenciar suas credenciais AWS. Abaixo estão algumas das opções disponíveis:

### Atualizar um perfil AWS

Você pode atualizar um perfil fornecendo os dados explicitamente usando a opção `--data`:

```shell
awscreds update --profile my_profile --data '{"aws_access_key_id": "123", "aws_secret_access_key": "456", "aws_session_token": "789"}'
```

Ou simplesmente ler os dados do clipboard (caso `--data` não seja fornecido):

```shell
awscreds update --profile my_profile
```

> **Nota**: Para o segundo exemplo, certifique-se de copiar as credenciais para o clipboard antes de executar o comando.

### Listar todos os perfis AWS existentes

Exibe uma lista de todos os perfis configurados no seu arquivo `~/.aws/credentials`:

```shell
awscreds list
```

### Deletar um perfil AWS

Você pode deletar um perfil específico com o comando:

```shell
awscreds delete
```

Ao executar este comando, você será solicitado a digitar o nome do perfil que deseja deletar.

## Usando com `pyenv` ou `virtualenv`

Caso você esteja utilizando `pyenv` ou `virtualenv`, lembre-se de ativar o ambiente virtual antes de usar os comandos `awscreds`:

```shell
pyenv activate aws-credentials-clipboard-updater
```

ou

```shell
source venv/bin/activate
```

Depois disso, todos os comandos `awscreds` estarão disponíveis enquanto o ambiente estiver ativo.

## Contribuição

Contribuições são bem-vindas! Se você deseja melhorar o projeto, abra um problema ou envie uma solicitação de pull no [repositório do GitHub](https://github.com/vavasilva/aws-credentials-clipboard-updater).

