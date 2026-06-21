# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from app_runtime import db


def BenchmarkTest46474():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % (db_value,)
    return render_template_string(data)
