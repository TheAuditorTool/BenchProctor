# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def ensure_str(value):
    return str(value)

def BenchmarkTest73923(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ensure_str(cookie_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
