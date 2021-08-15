from core import create_app
from core.extensions import db
import os

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# shell context
@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app,
        db=db
    )

# this clause is not needed since the file
# is called wsgi.py
# if __name__ == '__main__':
#     app.ru
