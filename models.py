from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship, sessionmaker
from sqlalchemy import String, Text, ForeignKey, create_engine


class Base(DeclarativeBase):

    id: Mapped[int] = mapped_column(primary_key=True)


class User(Base):

    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)

    posts: Mapped[list["Post"]] = relationship(back_populates="user")
    Comments: Mapped[list["Comment"]] = relationship(back_populates="user")


class Post(Base):

    __tablename__ = "posts"
    
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    user: Mapped["User"] = relationship(back_populates="posts")
    category: Mapped["Category"] = relationship(back_populates="posts")
    tags: Mapped[list["Tag"]] = relationship(secondary="post_tag", back_populates="posts")
    comments: Mapped[list["Post"]] = relationship(back_populates="post")



class Comment(Base):
    
    __tablename__ = "comments"

    content: Mapped[str] = mapped_column(nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    post: Mapped["Post"] = relationship(back_populates="comments")
    user: Mapped["User"] = relationship(back_populates="comments")


class Category(Base):

    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(unique=True)

    posts: Mapped["Post"] = relationship(back_populates="category")


class Tag(Base):

    __tablename__ = "tags"

    name: Mapped[str] = mapped_column(unique=True)\
    
    posts: Mapped[list["Post"]] = relationship(secondary="post_tag", back_populates="tags")


class PostTag(Base):

    __tablename__ = "post_tag"

    post_id = ForeignKey("posts.id")
    tag_id = ForeignKey("tags.id")


def get_session():
    engine = create_engine("sqlite:///blogon.db")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


session = get_session()