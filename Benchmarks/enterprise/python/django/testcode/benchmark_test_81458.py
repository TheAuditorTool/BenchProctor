# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest81458(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
