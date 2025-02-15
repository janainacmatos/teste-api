# Teste de API com Python e Requests

Este projeto contém um script em Python para testar a API pública [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts). O script realiza operações de GET e POST na API, validando as respostas e garantindo que a API esteja funcionando conforme o esperado.

## Estrutura do Projeto

- `teste_api.py`: Script principal que realiza os testes GET e POST.

## Funcionalidades

1. **Teste GET:**
   - Faz uma requisição GET para `/posts`.
   - Valida que a resposta é uma lista de posts.
   - Verifica que a lista não está vazia.
   - Verifica a presença dos campos `userId`, `id`, `title`, e `body` em cada post.

2. **Teste POST:**
   - Faz uma requisição POST para `/posts` com dados aleatórios gerados no script.
   - Valida que a resposta contém um ID único gerado pela API.
   - Assegura que o ID gerado é um inteiro.

## Como Usar

### Requisitos

- Python 3.x
- Biblioteca `requests`

### Instalação de Dependências

Certifique-se de ter a biblioteca `requests` instalada. Você pode instalá-la usando:

```bash
pip install requests
