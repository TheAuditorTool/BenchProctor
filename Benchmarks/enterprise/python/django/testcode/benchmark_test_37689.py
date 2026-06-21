# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37689(request):
    cookie_value = request.COOKIES.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
