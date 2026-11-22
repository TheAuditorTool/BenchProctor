# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest00201(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(data) + '</div>')
    return resp
