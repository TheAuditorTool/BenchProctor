# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def normalise_input(value):
    return value.strip()

def BenchmarkTest00894(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = normalise_input(cookie_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
