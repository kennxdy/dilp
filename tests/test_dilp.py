import unittest

from dilp import (
    get_meta,
    get_news,
    get_random,
    get_word,
    search_infix,
    search_near,
    search_prefix,
    search_suffix,
    search_word,
)


class TestDilp(unittest.TestCase):
    def test_get_news(self):
        result = get_news()
        if "title" in result[0]:
            title_exists = True
        self.assertEqual(title_exists, True, "Should be true")

    def test_get_news_with_limit(self):
        results = get_news(7)
        number_of_results = len(results)
        self.assertEqual(number_of_results, 7, "Should be 7")

    def test_get_meta(self):
        result = get_meta("first_word")
        first_word = result["first_word"]
        self.assertEqual(first_word, "a", "Should be a")

    def test_get_word(self):
        result = get_word()
        if "word_id" in result:
            id_exists = True
        self.assertEqual(id_exists, True, "Should be true")

    def test_get_random(self):
        result = get_random()
        if "word" in result:
            word_exists = True
        self.assertEqual(word_exists, True, "Should be true")

    def test_search_word(self):
        result = search_word("cavalo")
        word_id = result[0]["word_id"]
        self.assertEqual(word_id, 26842, "Should be 26842")

    def test_search_word_with_multiple_results(self):
        result = search_word("nona")
        if result:
            multiple_results = True
        self.assertEqual(multiple_results, True, "Should be true")

    def test_search_word_with_multiple_results_with_number_of_an_element(self):
        result = search_word("nona", 3)
        creator = result[0]["creator"]
        self.assertEqual(creator, "ambs", "Should be ambs")

    def test_search_prefix(self):
        result = search_prefix("pirom")
        word = result[0]["word"]
        self.assertEqual(word, "piromaco", "Should be piromaco")

    def test_search_infix(self):
        result = search_infix("pople")
        word = result[0]["word"]
        self.assertEqual(word, "apoplexia", "Should be apoplexia")

    def test_search_suffix(self):
        result = search_suffix("astrão")
        word = result[0]["word"]
        self.assertEqual(word, "canastrão", "Should be canastrão")

    def test_search_near(self):
        result = search_near("caralho")
        word = result[0]
        self.assertEqual(word, "baralho", "Should be baralho")


if __name__ == "__main__":
    unittest.main()
