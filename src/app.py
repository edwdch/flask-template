from flask import Flask
from route.index import router
from config.settings import settings

app = Flask(__name__)
app.register_blueprint(router, url_prefix="/api")

if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=settings.server_port())
