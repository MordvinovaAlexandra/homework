from datetime import datetime
from decimal import Decimal

class SearchResult:
    def __init__(self, title: str, price: Decimal, url: str, text: str, date: str) -> None:
        self.title = title
        self.price = price
        self.url = url
        self.text = text
        self.date = date

        self.created_at = datetime.todat()

class Search:
    def __init__(self, query: str, category: str = 'all', frequency: int = 24, notify: str = 'email') -> None:
        self.__query = query
        self.__category = category
        self.__frequency = frequency
        self.__notify = notify   

        self.results = set()
    
    def update(self, results: list[SearchResult]):
        self.__results.update(results)