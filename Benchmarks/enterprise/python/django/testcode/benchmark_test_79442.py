# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79442(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = f'{forwarded_ip:.200s}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
