# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37116(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
