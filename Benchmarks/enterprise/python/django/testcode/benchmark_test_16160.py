# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16160(request):
    cookie_value = request.COOKIES.get('session_token', '')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(cookie_value))
    return JsonResponse({'lookup': arr[idx]}, status=200)
