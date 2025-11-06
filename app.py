"""
Flask case manager that persists to PostgreSQL via SQLAlchemy.
Env variables used (in Kubernetes these will come from a Secret):
DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
"""


import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# Read DB connection values from environment
DB_HOST = os.environ.get('DB_HOST', 'pg-bank-postgresql')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = os.environ.get('DB_NAME', 'postgres')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password123') # placeholder


app.config['SQLALCHEMY_DATABASE_URI'] = (
f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Case(db.Model):
__tablename__ = 'cases'
id = db.Column(db.Integer, primary_key=True)
title = db.Column(db.String(255), nullable=False)
description = db.Column(db.Text, nullable=True)
status = db.Column(db.String(50), nullable=False, default='open')
created_at = db.Column(db.DateTime, default=datetime.utcnow)


def __repr__(self):
return f"<Case {self.id} {self.title}>"


@app.route('/', methods=['GET', 'POST'])
def index():
if request.method == 'POST':
title = request.form.get('title', '').strip()
description = request.form.get('description', '').strip()
if title:
c = Case(title=title, description=description)
db.session.add(c)
db.session.commit()
return redirect(url_for('index'))


cases = Case.query.order_by(Case.created_at.desc()).all()
return render_template('index.html', cases=cases)


@app.route('/close/<int:case_id>', methods=['POST'])
def close_case(case_id):
c = Case.query.get_or_404(case_id)
c.status = 'closed'
db.session.commit()
return redirect(url_for('index'))


if __name__ == '__main__':
with app.app_context():
db.create_all()
app.run(host='0.0.0.0', port=8080)
