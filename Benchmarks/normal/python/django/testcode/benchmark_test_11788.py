# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def relay_value(value):
    return value

def BenchmarkTest11788(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = relay_value(ua_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
