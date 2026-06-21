# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57610(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
