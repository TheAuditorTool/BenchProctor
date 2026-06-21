# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09079(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
