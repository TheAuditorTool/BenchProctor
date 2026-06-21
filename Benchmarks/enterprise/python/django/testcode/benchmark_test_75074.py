# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75074(request):
    host_value = request.META.get('HTTP_HOST', '')
    try:
        result = int(str(host_value))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
