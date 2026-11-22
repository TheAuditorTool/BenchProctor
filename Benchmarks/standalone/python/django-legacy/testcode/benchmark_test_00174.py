# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect
from app_runtime import db


def BenchmarkTest00174(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = bytes.fromhex(db_value).decode('utf-8', 'ignore')
    return redirect(str(data))
