from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Hello(Base):
    __tablename__ = "Hello"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))

    def __repr__(self) -> str:
        return f'Hello(id={self.id}, name={self.name})'