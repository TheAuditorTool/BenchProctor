# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify
from flask import current_app
from datetime import timedelta
from app_runtime import db


def BenchmarkTest79446():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ' '.join(str(db_value).split())
    current_app.permanent_session_lifetime = timedelta(seconds=1800)
    session.permanent = True
    session['data'] = str(data)
    return jsonify({"result": "success"})
