# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03327(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
