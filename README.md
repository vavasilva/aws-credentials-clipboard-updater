Claro, aqui está o README com o código dentro dos blocos de código:

```markdown
# AWS Credentials Clipboard Updater

O AWS Credentials Clipboard Updater é um utilitário de linha de comando (CLI) para gerenciar as credenciais da AWS. Este utilitário permite que você atualize, liste ou delete os perfis AWS no seu arquivo de credenciais.

## Instalação

### Ubuntu/Debian

1. Certifique-se de ter o Python instalado no seu sistema.
2. Clone o repositório do projeto:

   git clone https://github.com/vavasilva/aws-credentials-clipboard-updater.git
```

3. Navegue até o diretório do projeto:

   ```shell
   cd aws-credentials-clipboard-updater
   ```

4. Instale as dependências necessárias:

   ```shell
   pip install -r requirements.txt
   ```

5. Torne o CLI `awscreds` global executando o seguinte comando:

   ```shell
   pip install --editable .
   ```

### Arch Linux

1. Certifique-se de ter o Python instalado no seu sistema.
2. Clone o repositório do projeto:

   ```shell
   git clone https://github.com/vavasilva/aws-credentials-clipboard-updater.git
   ```

3. Navegue até o diretório do projeto:

   ```shell
   cd aws-credentials-clipboard-updater
   ```

4. Instale as dependências necessárias:

   ```shell
   pip install -r requirements.txt
   ```

5. Torne o CLI `awscreds` global executando o seguinte comando:

   ```shell
   pip install --editable .
   ```

### Dependências para Clipboard

Para garantir que as dependências específicas para manipulação de clipboard funcionem:

* No Arch Linux:
    ```
    sudo pacman -S xclip xsel
    ```

* Em distribuições baseadas no Debian/Ubuntu:
    ```
    sudo apt-get install xclip xsel
    ```

* Em distribuições baseadas no Red Hat/Fedora:
    ```
    sudo dnf install xclip xsel
    ```

## Uso

O CLI `awscreds` fornece as seguintes opções:

- Atualizar um perfil AWS:

  Agora, você pode usar o comando `update` de duas maneiras:

  1. Fornecer dados explicitamente usando a opção `--data`:
   
     ```shell
     awscreds update --profile my_profile --data '{"aws_access_key_id": "123", "aws_secret_access_key": "456", "aws_session_token": "789"}'
     ```
     
  2. Ler dados a partir do clipboard se a opção `--data` não for fornecida:
   
     ```shell
     awscreds update --profile my_profile
     ```
  
  No segundo caso, você deve ter as credenciais corretas no clipboard antes de executar o comando.

- Listar todos os perfis AWS existentes:

  ```shell
  awscreds list
  ```

  Este comando listará todos os perfis AWS disponíveis no seu arquivo de credenciais.

- Deletar um perfil AWS:

  ```shell
  awscreds delete
  ```

  Ao executar este comando, você será solicitado a digitar o nome do perfil AWS que deseja deletar.

Certifique-se de ter o Python corretamente instalado e as dependências satisfeitas para garantir que o CLI funcione corretamente.

## Contribuição

Contribuições são bem-vindas! Se você quiser melhorar o projeto, abra um problema ou envie uma solicitação de pull.
