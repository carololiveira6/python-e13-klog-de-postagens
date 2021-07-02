from app import db
from flask_sqlalchemy import SQLAlchemy

class KlogPosts(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(300), nullable=False)

    def __str__(self):
        return f"<{self.name} - {self.id}>"

    def __repr__(self):
        return f"<{self.name} - {self.id}>"
