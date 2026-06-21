# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28868(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = ' '.join(str(header_value).split())
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
