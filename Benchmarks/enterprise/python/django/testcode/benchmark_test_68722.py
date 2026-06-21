# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68722(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if str(header_value) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
