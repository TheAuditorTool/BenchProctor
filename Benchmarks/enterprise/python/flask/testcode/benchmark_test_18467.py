# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import base64
from app_runtime import db


def BenchmarkTest18467():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    return render_template_string(data)
