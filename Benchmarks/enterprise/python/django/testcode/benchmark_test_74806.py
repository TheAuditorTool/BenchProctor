# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def relay_value(value):
    return value

def BenchmarkTest74806(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = relay_value(cookie_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
