# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def relay_value(value):
    return value

def BenchmarkTest32872(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = relay_value(cookie_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
