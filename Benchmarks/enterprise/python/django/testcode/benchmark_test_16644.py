# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16644(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
