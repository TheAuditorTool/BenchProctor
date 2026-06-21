# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63570(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % str(cookie_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
