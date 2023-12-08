from typing import Optional

import requests

BASE_URL = "https://api.dicionario-aberto.net"


def get_news(limit: Optional[int] = None) -> list[str]:
    """Obter novidades, opcionalmente com limite ao número de itens."""
    payload = {"limit": limit}
    r = requests.get(f"{BASE_URL}/news", params=payload)
    return r.json()


def get_meta(key: str) -> dict[str, str]:
    """Permite obter alguns metadados.

    Args:
        count: Número de entradas no dicionário
        first_word: Primeira palavra do dicionário
         last_word: Última palavra do dicionário
        word: Identificador da palavra do dia

    Returns:
        Um dicionário com os metadados
    """
    r = requests.get(f"{BASE_URL}/metadata/{key}")
    return r.json()


def get_word() -> dict[str, str]:
    """Retorna a entrada em destaque (calculada cada 2 horas)."""
    r = requests.get(f"{BASE_URL}/wotd")
    return r.json()


def get_random() -> dict[str, str]:
    """Retorna uma entrada aleatória."""
    r = requests.get(f"{BASE_URL}/random")
    return r.json()


def search_word(name: str, number: Optional[int] = 0) -> list[str]:
    """
    Retorna a entrada correspondente ao verbete procurado. Se não for
    indicado o número de aceção e existirem mais que que uma, serão retornadas todas.
    """
    r = requests.get(f"{BASE_URL}/word/{name}/{number}")
    return r.json()


def search_prefix(name: str) -> list[str]:
    """
    Retorna uma lista das palavras que começam com a string indicada,
    juntamente com uma versão curta do verbete respetivo.
    """
    r = requests.get(f"{BASE_URL}/prefix/{name}")
    return r.json()


def search_infix(name: str) -> list[str]:
    """
    Retorna uma lista das palavras que incluem a string indicada,
    juntamente com uma versão curta do verbete respetivo.
    """
    r = requests.get(f"{BASE_URL}/infix/{name}")
    return r.json()


def search_suffix(name: str) -> list[str]:
    """
    Retorna uma lista das palavras que terminam na string indicada,
    juntamente com uma versão curta do verbete respetivo.
    """
    r = requests.get(f"{BASE_URL}/suffix/{name}")
    return r.json()


def search_near(name: str) -> list[str]:
    """Retorna uma lista de palavras próximas, com distância de Levenshtein 1."""
    r = requests.get(f"{BASE_URL}/near/{name}")
    return r.json()
