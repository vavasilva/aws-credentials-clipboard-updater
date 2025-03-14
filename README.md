# AWS Credentials Clipboard Updater

O AWS Credentials Clipboard Updater é um utilitário de linha de comando (CLI) para gerenciar as credenciais da AWS. Ele permite atualizar, listar ou deletar perfis no seu arquivo de credenciais AWS de maneira prática e intuitiva.

## Instalação

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)
- Para funcionalidades de clipboard: dependências específicas por sistema operacional (ver abaixo)

### Instalação Global

Para instalar o AWS Credentials Clipboard Updater globalmente no seu sistema, execute:

```shell
pip install git+https://github.com/vavasilva/aws-credentials-clipboard-updater.git
```

Após a instalação, o comando `awscreds` estará disponível em qualquer diretório do seu sistema.

> **Nota**: Em alguns sistemas, pode ser necessário usar `pip3` em vez de `pip` ou adicionar a flag `--user` para instalação sem privilégios de administrador (`pip install --user git+https://github.com/vavasilva/aws-credentials-clipboard-updater.git`).

### Instalação para Desenvolvimento

Se você deseja contribuir para o projeto ou fazer modificações no código, siga estas etapas:

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
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

##### Utilizando `pyenv` com `pyenv-virtualenv`:
```shell
pyenv virtualenv 3.12.0 aws-credentials-clipboard-updater
pyenv activate aws-credentials-clipboard-updater
```

#### 4. Instale o projeto em modo desenvolvimento:
Instale o projeto no modo editável para que suas alterações sejam refletidas imediatamente:

```shell
pip install -e .
```

### Dependências para Clipboard

Para garantir que as funcionalidades de clipboard funcionem corretamente, você pode precisar instalar pacotes adicionais de acordo com o seu sistema operacional:

- **macOS**: Não requer pacotes adicionais

- **Windows**: Não requer pacotes adicionais

- **Linux**:
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
