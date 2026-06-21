# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def relay_value(value):
    return value

def BenchmarkTest81184(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = relay_value(forwarded_ip)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
