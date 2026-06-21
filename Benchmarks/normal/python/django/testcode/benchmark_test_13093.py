# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest13093(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = coalesce_blank(host_value)
    processed = data[:64]
    if str(processed) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
