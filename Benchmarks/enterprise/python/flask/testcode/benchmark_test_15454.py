# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import urllib.parse
from app_runtime import db


def BenchmarkTest15454():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value}'
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
