# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24145(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
