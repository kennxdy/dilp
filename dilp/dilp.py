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
