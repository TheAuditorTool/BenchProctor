# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39004(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = ' '.join(str(host_value).split())
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
