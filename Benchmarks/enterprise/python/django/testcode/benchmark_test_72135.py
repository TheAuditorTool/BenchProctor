# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72135(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return JsonResponse({'error': 'zero division'}, status=400)
    result = 100 / divisor
    return JsonResponse({"saved": True})
