from flask import Blueprint, request, render_template

from app import db

bp = Blueprint("bp_posts", __name__)

@bp.route("/posts", methods=["GET"])
def return_form():
    ...

@bp.route("/api/posts", methods=["POST"])
def post_form():
    ...

@bp.route("/api/posts", methods=["GET"])
def get_form():
    ...

@bp.route("/api/posts/<post_id>", methods=["GET"])
def post_by_id():
    ...