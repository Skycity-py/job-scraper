from flask_frozen import Freezer
from main import app

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

@freezer.register_generator
def search():
    keywords = ["python", "java", "javascript"]
    for keyword in keywords:
        yield {'keyword': keyword}

if __name__ == '__main__':
    freezer.freeze()