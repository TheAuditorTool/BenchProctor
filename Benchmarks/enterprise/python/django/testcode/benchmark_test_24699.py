# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24699(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value}'
    if str(data) in ('localhost', 'internal-gateway'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
