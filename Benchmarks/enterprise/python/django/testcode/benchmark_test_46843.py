# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46843(request):
    cookie_value = request.COOKIES.get('session_token', '')
    try:
        result = int(str(cookie_value))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
