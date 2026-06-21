# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59823(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '{}'.format(cookie_value)
    eval(str(data))
    return JsonResponse({"saved": True})
