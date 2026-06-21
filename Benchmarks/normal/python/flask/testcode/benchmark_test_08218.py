# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from app_runtime import db


def BenchmarkTest08218():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = bytes.fromhex(db_value).decode('utf-8', 'ignore')
    return redirect(str(data))
