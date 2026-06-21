# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45738(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
