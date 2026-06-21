# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from app_runtime import db


def BenchmarkTest00283():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % str(db_value)
    return redirect(str(data))
