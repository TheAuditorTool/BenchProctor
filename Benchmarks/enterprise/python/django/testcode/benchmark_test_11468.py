# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11468(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
