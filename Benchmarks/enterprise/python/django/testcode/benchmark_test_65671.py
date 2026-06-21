# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65671(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    divisor = int(str(header_value)) if str(header_value).isdigit() else 1
    if divisor == 0:
        return JsonResponse({'error': 'zero division'}, status=400)
    result = 100 / divisor
    return JsonResponse({"saved": True})
