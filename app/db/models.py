from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from pgvector.sqlalchemy import Vector

from app.db.database import Base

class Chunk(Base):
    __tablename__ = "chunks"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    document_id: Mapped[str] = mapped_column(String(255), nullable=False)
    source_url: Mapped[str] = mapped_column(Text, nullable=False)

    department: Mapped[str] = mapped_column(String(100), nullable=False)
    access_level: Mapped[str] = mapped_column(String(50), nullable=False)

    chunk_index: Mapped[int] = mapped_column(nullable=False)

    embedding: Mapped[list[float]] = mapped_column(Vector(384))