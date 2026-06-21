# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from app_runtime import db


def BenchmarkTest00801():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    return redirect(str(data))
