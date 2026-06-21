# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39730(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
