# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01563(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ua_value if ua_value else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
