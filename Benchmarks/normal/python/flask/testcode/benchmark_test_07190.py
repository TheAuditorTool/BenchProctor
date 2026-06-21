# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
from app_runtime import db, User


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest07190():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(db_value)
    data = reader()
    db.session.query(User).filter(User.id == data).all()
    return jsonify({"result": "success"})
