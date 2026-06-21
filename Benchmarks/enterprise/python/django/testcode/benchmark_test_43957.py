# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43957(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
