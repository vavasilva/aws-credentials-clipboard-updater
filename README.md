```markdown
# AWS Credentials Clipboard Updater

O AWS Credentials Clipboard Updater é um utilitário de linha de comando (CLI) para atualizar as credenciais da AWS com base no conteúdo da área de transferência.

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

Para usar o CLI `awscreds` e atualizar as credenciais da AWS, execute o seguinte comando:

```shell
awscreds
```

Isso irá chamar a função `update_aws_credentials` e exibirá uma mensagem de prompt solicitando que você digite o nome do perfil AWS que deseja atualizar.

Certifique-se de ter o Python corretamente instalado e as dependências satisfeitas para garantir que o CLI funcione corretamente.

## Contribuição

Contribuições são bem-vindas! Se você quiser melhorar o projeto, abra um problema ou envie uma solicitação de pull.

## Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).
