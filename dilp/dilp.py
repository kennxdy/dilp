from typing import Optional

import requests

BASE_URL = "https://api.dicionario-aberto.net"


def get_news(limit: Optional[int] = None) -> list[str]:
    payload = {"limit": limit}
    r = requests.get(f"{BASE_URL}/news", params=payload)
    return r.json()


def get_meta(key: str) -> dict[str, str]:
    r = requests.get(f"{BASE_URL}/metadata/{key}")
    return r.json()


def get_word() -> dict[str, str]:
    r = requests.get(f"{BASE_URL}/wotd")
    return r.json()


def get_random() -> dict[str, str]:
    r = requests.get(f"{BASE_URL}/random")
    return r.json()


def search_word(name: str, number: Optional[int] = 0) -> list[str]:
    r = requests.get(f"{BASE_URL}/word/{name}/{number}")
    return r.json()


def search_prefix(name: str) -> list[str]:
    r = requests.get(f"{BASE_URL}/prefix/{name}")
    return r.json()


def search_infix(name: str) -> list[str]:
    r = requests.get(f"{BASE_URL}/infix/{name}")
    return r.json()


def search_suffix(name: str) -> list[str]:
    r = requests.get(f"{BASE_URL}/suffix/{name}")
    return r.json()


def search_near(name: str) -> list[str]:
    r = requests.get(f"{BASE_URL}/near/{name}")
    return r.json()
