# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37355(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = (lambda v: v.strip())(header_value)
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return JsonResponse({'error': 'zero division'}, status=400)
    result = 100 / divisor
    return JsonResponse({"saved": True})
