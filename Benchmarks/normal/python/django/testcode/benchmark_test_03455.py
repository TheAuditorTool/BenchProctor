# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03455(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
