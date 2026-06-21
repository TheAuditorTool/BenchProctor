# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00870(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % (origin_value,)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
