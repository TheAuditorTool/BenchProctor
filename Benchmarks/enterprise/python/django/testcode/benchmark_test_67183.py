# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest67183(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    parts = []
    for token in str(profile_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
