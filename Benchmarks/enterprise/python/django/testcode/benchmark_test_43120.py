# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43120(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '%s' % (header_value,)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
