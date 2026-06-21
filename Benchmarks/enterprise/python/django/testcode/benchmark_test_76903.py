# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def coalesce_blank(value):
    return value or ''

def BenchmarkTest76903(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = coalesce_blank(referer_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
