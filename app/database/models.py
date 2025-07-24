from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship, sessionmaker
from sqlalchemy import Text, ForeignKey, create_engine, func


class BaseModel(DeclarativeBase):

    id: Mapped[int] = mapped_column(primary_key=True)


class PostModel(BaseModel):

    __tablename__ = "posts"
    
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(Text)
    published: Mapped[bool] = mapped_column(server_default="TRUE")
    # user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    create_date: Mapped[datetime] = mapped_column(
        server_default=func.current_timestamp(), nullable=False
    )

    # user: Mapped["User"] = relationship(back_populates="posts")
    # tags: Mapped[list["Tag"]] = relationship(secondary="post_tag", back_populates="posts")
    # comments: Mapped[list["Post"]] = relationship(back_populates="post")


class UserModel(BaseModel):

    __tablename__ = "users"

    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    create_date: Mapped[datetime] = mapped_column(
        server_default=func.current_timestamp(), nullable=False
    )

#     posts: Mapped[list["Post"]] = relationship(back_populates="user")
#     Comments: Mapped[list["Comment"]] = relationship(back_populates="user")


# class Comment(Base):
    
#     __tablename__ = "comments"

#     content: Mapped[str] = mapped_column(nullable=False)
#     post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     create_date: Mapped[datetime] = mapped_column(
#         server_default=func.current_timestamp(), nullable=False
#     )

#     post: Mapped["Post"] = relationship(back_populates="comments")
#     user: Mapped["User"] = relationship(back_populates="comments")


# class Tag(Base):

#     __tablename__ = "tags"

#     name: Mapped[str] = mapped_column(unique=True)
#     create_date: Mapped[datetime] = mapped_column(
#         server_default=func.current_timestamp(), nullable=False
#     )
    
#     posts: Mapped[list["Post"]] = relationship(secondary="post_tag", back_populates="tags")


# class PostTag(Base):

#     __tablename__ = "post_tag"

#     post_id = ForeignKey("posts.id")
#     tag_id = ForeignKey("tags.id")


# def get_session():
#     engine = create_engine("sqlite:///blogon.db")
#     Base.metadata.create_all(engine)
#     Session = sessionmaker(bind=engine)
#     return Session()


# session = get_session()