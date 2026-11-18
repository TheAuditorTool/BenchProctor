# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect
from app_runtime import db


def BenchmarkTest00102(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    kind = 'json' if str(db_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(db_value).strip()
        case _:
            data = str(db_value)
    return redirect(str(data))
