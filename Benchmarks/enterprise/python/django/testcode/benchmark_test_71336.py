# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71336(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return JsonResponse({'error': 'zero division'}, status=400)
    result = 100 / divisor
    return JsonResponse({"saved": True})
