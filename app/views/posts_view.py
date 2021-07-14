from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, request, render_template
from app.models.posts_model import KlogPosts
from app import db

bp = Blueprint("bp_posts", __name__)

@bp.route("/posts", methods=["GET"])
def return_form():
    
    posts = KlogPosts()

    query = posts.query.all()

    return {
        "postagens": [
            {
                "id": posts.id,
                "name": posts.name,
                "title": posts.title,
                "text": posts.text
            }
            for posts in query
        ]
    }

@bp.route("/api/posts", methods=["GET, POST"])
def post_get_form():
    
    if request.method == "POST":
        form_data = request.get_json()

        posts = KlogPosts(**form_data)

        db.session.add(posts)
        db.session.commit()

        return "Oi"

@bp.route("/api/posts/<post_id>", methods=["GET"])
def post_by_id(post_id):
    
    posts_id = KlogPosts.query.get(post_id)

    return posts_id