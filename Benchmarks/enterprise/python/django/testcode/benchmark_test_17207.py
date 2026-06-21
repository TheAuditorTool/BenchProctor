# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17207(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
