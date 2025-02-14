import requests
import random
import string

def get_random_string(length=10):
    """Gera uma string aleatória de caracteres alfanuméricos."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def test_get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx

        data = response.json()
        assert isinstance(data, list), "A resposta não é uma lista de posts."
        assert len(data) > 0, "A lista de posts está vazia."

        # Opcional: Validar estruturas dos itens
        first_post = data[0]
        assert "userId" in first_post, "Campo 'userId' ausente no post."
        assert "id" in first_post, "Campo 'id' ausente no post."
        assert "title" in first_post, "Campo 'title' ausente no post."
        assert "body" in first_post, "Campo 'body' ausente no post."

        print("Teste GET passou com sucesso!")

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição GET: {e}")
    except AssertionError as e:
        print(f"Erro de validação em GET: {e}")

def test_post_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    post_data = {
        "title": get_random_string(),
        "body": get_random_string(50),
        "userId": random.randint(1, 10)
    }

    try:
        response = requests.post(url, json=post_data)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx

        data = response.json()
        assert "id" in data, "O retorno não contém um ID."
        assert isinstance(data["id"], int), "O ID gerado não é um inteiro."

        print("Teste POST passou com sucesso!")

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição POST: {e}")
    except AssertionError as e:
        print(f"Erro de validação em POST: {e}")

def run_tests():
    test_get_posts()
    test_post_post()

if __name__ == "__main__":
    run_tests()