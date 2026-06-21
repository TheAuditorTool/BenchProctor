# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest00611(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = default_blank(ua_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
