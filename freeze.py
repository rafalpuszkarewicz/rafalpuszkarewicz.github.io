from flask_frozen import Freezer
from cover.app import app

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()