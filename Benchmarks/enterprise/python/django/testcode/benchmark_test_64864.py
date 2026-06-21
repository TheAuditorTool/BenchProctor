# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest64864(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(profile_value)
    data = collected
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
