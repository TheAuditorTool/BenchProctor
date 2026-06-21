# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def coalesce_blank(value):
    return value or ''

def BenchmarkTest46609(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = coalesce_blank(origin_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
