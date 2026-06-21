# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32239(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
