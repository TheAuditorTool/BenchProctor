# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42916(request):
    user_id = request.GET.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
