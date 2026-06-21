# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest79787(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    prefix = ''
    data = prefix + str(profile_value)
    request.session.clear()
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
