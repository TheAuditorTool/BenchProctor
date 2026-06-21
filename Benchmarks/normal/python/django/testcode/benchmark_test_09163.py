# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09163(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
