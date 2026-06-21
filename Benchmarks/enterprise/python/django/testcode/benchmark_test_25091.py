# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25091(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
