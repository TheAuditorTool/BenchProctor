# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42636(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = str(origin_value).replace('\x00', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
