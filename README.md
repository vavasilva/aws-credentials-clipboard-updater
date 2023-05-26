```markdown
# AWS Credentials Clipboard Updater

O AWS Credentials Clipboard Updater é um utilitário de linha de comando (CLI) para gerenciar as credenciais da AWS. Este utilitário permite que você atualize, liste ou delete os perfis AWS no seu arquivo de credenciais.

## Instalação

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

## Uso

O CLI `awscreds` fornece as seguintes opções:

- Atualizar um perfil AWS:

  ```shell
  awscreds update
  ```

  Ao executar este comando, você será solicitado a digitar o nome do perfil AWS que deseja atualizar e os dados das credenciais em formato JSON.

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
