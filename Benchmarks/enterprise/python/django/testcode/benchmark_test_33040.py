# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33040(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % (origin_value,)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
