# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10799(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value}'
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
