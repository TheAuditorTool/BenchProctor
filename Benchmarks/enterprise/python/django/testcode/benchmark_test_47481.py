# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47481(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return JsonResponse({"saved": True})
