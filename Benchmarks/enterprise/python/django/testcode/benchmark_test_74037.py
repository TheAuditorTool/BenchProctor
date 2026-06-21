# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74037(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
