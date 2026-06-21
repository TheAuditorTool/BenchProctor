# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29006(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    prefix = ''
    data = prefix + str(ua_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
