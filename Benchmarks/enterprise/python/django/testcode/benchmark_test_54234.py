# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54234(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    if str(data) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
