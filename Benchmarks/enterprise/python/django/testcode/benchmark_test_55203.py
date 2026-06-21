# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest55203(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    if profile_value:
        data = profile_value
    else:
        data = ''
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
