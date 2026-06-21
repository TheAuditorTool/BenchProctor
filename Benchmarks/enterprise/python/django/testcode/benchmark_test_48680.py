# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48680(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
