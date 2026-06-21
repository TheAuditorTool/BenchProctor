# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def coalesce_blank(value):
    return value or ''

def BenchmarkTest13783(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = coalesce_blank(host_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
