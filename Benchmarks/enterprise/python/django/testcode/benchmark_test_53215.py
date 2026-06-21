# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53215(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = ' '.join(str(forwarded_ip).split())
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
