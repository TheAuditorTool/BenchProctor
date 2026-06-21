# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76394(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
