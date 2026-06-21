# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51128(request):
    user_id = request.GET.get('id', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(user_id))
    return resp
