# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from app_runtime import db


def BenchmarkTest80822():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(db_value).split(',')
    data = ','.join(parts)
    return render_template_string(data)
