# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from app_runtime import db


def BenchmarkTest75932():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return render_template_string(data)
