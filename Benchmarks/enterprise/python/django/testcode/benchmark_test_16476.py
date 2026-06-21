# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16476(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '{}'.format(cookie_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
