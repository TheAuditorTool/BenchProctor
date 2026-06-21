# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36696(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
