from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Uuid, text, ForeignKey, Text


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(db.Model):
    __tablename__ = "users"
    id: Mapped[Uuid.UUID] = mapped_column(
        Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    username: Mapped[str] = mapped_column(String(50), unique=True)
    name: Mapped[str] = mapped_column(String(150))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))


class Meme(db.Model):
    __tablename__ = "memes"
    id: Mapped[Uuid.UUID] = mapped_column(
        Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    user_id: Mapped[Uuid.UUID] = mapped_column(ForeignKey("users.id"))
    storage_url: Mapped[str] = mapped_column(Text)
    raw_caption: Mapped[str] = mapped_column(Text)
    ocr_text: Mapped[str] = mapped_column(Text)


class Prediction(db.Model):
    __tablename__ = "predictions"
    id: Mapped[Uuid.UUID] = mapped_column(
        Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )


class MemeFeature(db.Model):
    __tablename__ = "meme_features"
    id: Mapped[Uuid.UUID] = mapped_column(
        Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
