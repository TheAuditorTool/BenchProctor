# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03832(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % str(cookie_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
