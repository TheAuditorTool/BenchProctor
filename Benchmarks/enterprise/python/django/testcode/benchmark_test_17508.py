# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17508(request):
    host_value = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
