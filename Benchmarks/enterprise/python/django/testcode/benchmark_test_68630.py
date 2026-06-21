# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68630(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = f'{header_value}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
