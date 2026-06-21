# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72297(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
