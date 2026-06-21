# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66055(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
