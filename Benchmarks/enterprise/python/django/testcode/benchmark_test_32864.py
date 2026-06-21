# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32864(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = header_value if header_value else 'default'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
