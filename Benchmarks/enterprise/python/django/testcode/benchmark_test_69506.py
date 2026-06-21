# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69506(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
