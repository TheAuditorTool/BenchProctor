# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22365(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        result = int(str(ua_value))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
