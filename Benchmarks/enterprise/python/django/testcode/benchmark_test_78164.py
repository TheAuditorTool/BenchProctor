# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import defusedxml.ElementTree


def BenchmarkTest78164(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
