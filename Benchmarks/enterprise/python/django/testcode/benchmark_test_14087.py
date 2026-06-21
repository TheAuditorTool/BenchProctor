# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest14087(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(profile_value), max_age=86400)
    return resp
