from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from model import Search



class AbstractRepository(ABC):
    @abstractmethod
    def add(self, search: Search) -> None:
        raise NotImplementedError
    
    def get(self, search_id: int) -> Search | None:
        raise NotImplementedError
    
    def list(self) -> list[Search]:
        raise NotImplementedError
    
class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session):
        self.__session = session

    def add(self, search: Search) -> None:
        self.__session.add(search) #добавление в поиск
    
    def get(self, search_id: int) -> Search | None:
        return self.__session.query(Search).filter_by(id=search_id).one_or_none()
    
    def list(self) -> list[Search]:
        return self.__session.query(Search).all()
    