# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00493(request):
    user_id = request.GET.get('id', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(user_id), secure=True, httponly=True, samesite='Strict')
    return resp
