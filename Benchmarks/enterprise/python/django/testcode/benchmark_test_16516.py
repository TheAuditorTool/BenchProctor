# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16516(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
