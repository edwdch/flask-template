from flask import Blueprint

router = Blueprint("app", __name__)


@router.get("/ping")
def ping():
    return {"ping": "pong"}
