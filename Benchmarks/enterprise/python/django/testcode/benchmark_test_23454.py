# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23454(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if cookie_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = cookie_value
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(processed)})
