# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20790(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
