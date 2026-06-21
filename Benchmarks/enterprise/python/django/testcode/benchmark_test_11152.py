# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11152(request):
    cookie_value = request.COOKIES.get('session_token', '')
    raise RuntimeError('processing failed: ' + str(cookie_value))
    return JsonResponse({"saved": True})
