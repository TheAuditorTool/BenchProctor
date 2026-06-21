# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80471(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(header_value))
    return resp
