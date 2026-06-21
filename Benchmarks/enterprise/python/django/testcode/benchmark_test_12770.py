# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest12770(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
