# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import base64
from app_runtime import db


def BenchmarkTest04642():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    return redirect(str(data))
