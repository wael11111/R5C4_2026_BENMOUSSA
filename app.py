from pathlib import Path

from flask import Flask

from app.controllers.parties_controller import create_controller


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "parties.db"

app = Flask(__name__)

app.register_blueprint(create_controller(DB_PATH))


if __name__ == "__main__":
    app.run(debug=True)