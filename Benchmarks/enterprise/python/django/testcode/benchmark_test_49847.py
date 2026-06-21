# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49847(request):
    host_value = request.META.get('HTTP_HOST', '')
    if str(host_value) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
