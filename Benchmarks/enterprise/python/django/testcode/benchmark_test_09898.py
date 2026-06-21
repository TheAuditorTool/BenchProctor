# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09898(request):
    cookie_value = request.COOKIES.get('session_token', '')
    match str(cookie_value):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
