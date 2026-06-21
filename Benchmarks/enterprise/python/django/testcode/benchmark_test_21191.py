# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21191(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
