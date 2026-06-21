# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67537(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if str(origin_value) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
