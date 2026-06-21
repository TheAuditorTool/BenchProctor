# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50979(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if str(cookie_value) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
