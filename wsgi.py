"""App entry point."""
from flask_wtf_tutorial import create_app, db
from flask_wtf_tutorial.models import User, Post

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
