# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14751(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = str(ua_value).replace('\x00', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
