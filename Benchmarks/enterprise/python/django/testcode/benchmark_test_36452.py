# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest36452(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = to_text(cookie_value)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
