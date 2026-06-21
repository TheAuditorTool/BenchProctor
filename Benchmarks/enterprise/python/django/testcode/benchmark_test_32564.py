# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32564(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
