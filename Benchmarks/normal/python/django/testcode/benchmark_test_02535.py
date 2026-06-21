# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02535(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value}'
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JsonResponse({'lookup': arr[idx]}, status=200)
