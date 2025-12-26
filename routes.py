from flask import Blueprint, request, jsonify
from models import db, Comment, Task
from models import Task


comment_bp = Blueprint("comments", __name__)

# CREATE comment
@comment_bp.route("/tasks/<int:task_id>/comments", methods=["POST"])
def add_comment(task_id):
    data = request.get_json()

    comment = Comment(
        content=data["content"],
        task_id=task_id
    )

    db.session.add(comment)
    db.session.commit()

    return jsonify({"id": comment.id, "content": comment.content}), 201


# READ comments for a task
@comment_bp.route("/tasks/<int:task_id>/comments", methods=["GET"])
def get_comments(task_id):
    comments = Comment.query.filter_by(task_id=task_id).all()

    return jsonify([
        {"id": c.id, "content": c.content}
        for c in comments
    ]), 200


# UPDATE comment
@comment_bp.route("/comments/<int:comment_id>", methods=["PUT"])
def update_comment(comment_id):
    data = request.get_json()
    comment = Comment.query.get_or_404(comment_id)

    comment.content = data["content"]
    db.session.commit()

    return jsonify({"id": comment.id, "content": comment.content}), 200


# DELETE comment
@comment_bp.route("/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    db.session.delete(comment)
    db.session.commit()

    return jsonify({"message": "Comment deleted"}), 200

# CREATE task
@comment_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    task = Task(title=data["title"])
    db.session.add(task)
    db.session.commit()
    return {"id": task.id, "title": task.title}, 201


# READ all tasks
@comment_bp.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return [{"id": t.id, "title": t.title} for t in tasks], 200


# UPDATE task
@comment_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    task = Task.query.get_or_404(task_id)
    task.title = data["title"]
    db.session.commit()
    return {"id": task.id, "title": task.title}, 200


# DELETE task
@comment_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return {"message": "Task deleted"}, 200
