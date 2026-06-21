# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19849(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
