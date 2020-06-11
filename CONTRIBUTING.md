# Contributing

> Pode contribuir a vontade, você será sempre bem-vindo(a). Mas temos algumas regras para serem seguidas.

- [Adicionar/atualizar funcionalidades](#Adicionaratualizar-funcionalidades)
- [Criando uma issue](#Criando-uma-issue)
- [Clonar o repositório](#Clonar-o-repositório)
- [Contribuir com implementação](#Contribuir-com-implementação)
- [Realizando uma Pull Request - PR](#Realizando-uma-Pull-Request---PR)

## Adicionar/Atualizar funcionalidades

Você olhou a aplicação e pensou em alguma funcionalidade que deveria ser adicionada no projeto ? :open_mouth:

**_Então, você tem duas opções:_**

- [Abrir uma issue detalhando sua ideia](#criando-uma-issue)
- [Você mesmo implementar a funcionalidade](#contribuir-com-implementação)

## Criando uma issue

Na página do [projeto](https://github.com/Rickecr/PyGraph), você pode clicar no botão `Issues` e na página irá aparecer um botão `new issue`, então é só selecionar e seguir os seguintes passos:

- Selecione o tipo da sua issue: `Bug ou Feature`.
- Dê um bom nome a sua issue.
- Detalhe bem sobre qual objetivo da issue.
- Imagens caso possível.
- Selecione labels para sua issue.
- Por fim, clique em `Submit new issue`.

## Clonar o repositório

Na página inicial do [repositório](https://github.com/Rickecr/happy_download) tem um botão `Fork`. Ao clicar é só esperar concluir o fork. E então ele irá criar o repositório na sua conta. E agora é só clonar em sua máquina, assim:

```sh
git clone https://github.com/<nome_de_usuario>/happy_download
```

Ao concluir, você terá o repositório em seu computador e então é só abrir em seu editor preferido e fazer suas modificações.

Ao terminar suas modificações, você deve commitar suas alterações, mas primeiro:

```sh
git add .
```

O comando acima irá preparar todos os arquivos modificados para serem commitados, passando por todas as alterações que foram feitas por você onde decedirá se a alteração será adicionada (você deve estar dentro da pasta do projeto para usar o comando). Agora é só commitar as alterações:

```sh
git commit -m "<Sua_Mensagem>"
```

E por fim, você irá enviar as alterações para o repositório remoto:

```sh
git push origin master
```

Mas isso só irá alterar no seu fork, o repositório oficial não vai ter suas alterações e agora ? :confused:

Calma, agora que entra o `Pull Request` ou `PR`

## Contribuir com implementação:

Depois de ter realizado o fork e o clone do projeto, escolhido seu editor de texto favorito, nós amamos o VSCode, mas fique a vontade para escolher o seu. Então é hora da codificação.

Mas calma ai, antes de qualquer coisa, você deve escolher uma issue que pretender trabalhar. Se a issue que trata sobre a funcionalidade não existir, você deve criar e dizer que esta trabalhando nela, caso ela exista você deve dizer lá(caso não já tenha alguém) que pretende trabalhar na issue. E após feito isso, agora sim você está pronto para codificação.

Entenda como é a [estrutura do projeto](#Entendendo-as-pastas), o que cada arquivo é responsável.

Consiga seu próprio [token de acesso](#como-conseguir-seu-token)

### Entendendo as pastas:

Todo o código da aplicação se encontra na pasta `src`.

- Na pasta de `config` estão todos os arquivos de configuração do projeto.

  - Você precisa criar um arquivo `.env`(igual o arquivo `.env-example`) e adicionar o token para conseguir utiliza o bot. Você deve ter seu próprio token.
  - No arquivo `settings.py` estão as variáveis que serão importadas por outros arquivos.

- Na raiz, o arquivo `utils` é onde fica as funções que serão utilizadas na aplicação, como: baixar um vídeo.

- Na raiz, o arquivo `core` onde fica o principal código do sistema.

### Como conseguir seu token:

Você deve iniciar uma conversa com o bot: [BotFather](https://telegram.me/BotFather)

Utilize o comando: `/newbot` para criar um novo bot e siga os passos.

No final o bot irá retornar um token de acesso, é esse token que você vai poder usar para testar suas funcionalidades.

Copie esse token e cole no arquivo `.env` e então tudo passara a funcionar com esse bot que você criou.

### Realizar a PR

E agora você está pronto para realizar sua PR e ser feliz com o mundo OpenSource.

## Realizando uma Pull Request - PR

Na página do seu fork irá aparecer uma mensagem em amarelo solicitando que você faça uma Pull Request para o repositório original. Ao clicar irá abrir uma página para você preencher as informações sobre sua PR.

- Referencie a issue em que você está trabalhando usando `#<numero_da_issue>`

- Descreva suas modificações

- Espere pela avaliação da sua PR, e pode ocorrer de pedimos algumas alterações a seres feitas
