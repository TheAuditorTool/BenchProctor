# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect
from app_runtime import db


def BenchmarkTest00644(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return redirect(str(data))
