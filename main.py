from flask import Flask, render_template
from data import db_session
from data.user import User
from data.jobs import Jobs

app = Flask(__name__)
db_session.global_init(f"db/mars.db")
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    return render_template("index.html", news=jobs)


def main():
    app.run()
    # db_sess = db_session.create_session()
    # user = db_sess.query(User).first()
    # print(user.id)


if __name__ == '__main__':
    main()
