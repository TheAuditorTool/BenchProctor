# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01161(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(ua_value)})
