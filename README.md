# AWS Credentials Updater

Este projeto fornece uma ferramenta de linha de comando (CLI) em Python para atualizar o arquivo .aws/credentials com base em um JSON copiado no clipboard. A ferramenta é útil quando você deseja atualizar rapidamente suas credenciais da AWS sem editar manualmente o arquivo.

## Pré-requisitos

- Python 3.6 ou superior
- Pip (gerenciador de pacotes do Python)

## Instalação

Clone este repositório e instale as dependências necessárias:

```bash
git clone https://github.com/seu_usuario/aws-credentials-updater.git
cd aws-credentials-updater
pip install -r requirements.txt
```

## Tornar o CLI global

Para tornar o CLI global e executá-lo em qualquer lugar do terminal, siga os passos abaixo:

1. Torne o arquivo `awscreds.py` executável:

```bash
chmod +x awscreds.py
```

3. Mova o arquivo para um diretório que esteja no seu `PATH`. Um local comum para scripts personalizados é o diretório `~/.local/bin`:

```bash
mv awscreds ~/.local/bin
```

Se o diretório `~/.local/bin` não estiver no seu `PATH`, você pode adicioná-lo. Abra o arquivo `~/.bashrc` (ou `~/.zshrc` se estiver usando Zsh) e adicione a seguinte linha:

```bash
export PATH=$PATH:~/.local/bin
```

4. Atualize as variáveis de ambiente do seu shell atual:

```bash
source ~/.bashrc
```

(ou `source ~/.zshrc` se estiver usando Zsh)

Agora você deve ser capaz de executar o comando `awscreds` de qualquer lugar no seu terminal. Lembre-se de que, para tornar essa configuração permanente, você deve seguir os passos acima para todos os ambientes e usuários nos quais deseja usar o CLI globalmente.

## Uso

1. Copie o JSON com as informações das credenciais da AWS para o clipboard. O JSON deve ter a seguinte estrutura:

```json
{
    "aws_account": "arn:aws:iam::XXXXXX:role/poweruser",
    "aws_access_key_id": "88888",
    "aws_secret_access_key": "99999",
    "aws_session_token": "999",
    "aws_session_expiration": "17/05/2023 17:29:13"
}
```

2. Execute a ferramenta de linha de comando:

```bash
awscreds
```

3. Digite o nome do perfil que você deseja atualizar quando solicitado.

A ferramenta atualizará o arquivo .aws/credentials com as novas informações do perfil fornecido.

## Limitações

- Esta ferramenta foi desenvolvida e testada em ambientes Linux e macOS. Pode funcionar no Windows, mas não foi testada nesse sistema operacional.
- O JSON copiado para o clipboard deve conter todas as chaves necessárias (`aws_access_key_id`, `aws_secret_access_key` e `aws_session_token`), caso contrário, a ferramenta mostrará um erro.

## Contribuições

Contribuições são bem-vindas