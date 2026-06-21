# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest04376(request):
    cookie_value = request.COOKIES.get('session_token', '')
    defusedxml.ElementTree.fromstring(str(cookie_value))
    return JsonResponse({"saved": True})
