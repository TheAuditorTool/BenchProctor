# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest61813(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    defusedxml.ElementTree.fromstring(str(referer_value))
    return JsonResponse({"saved": True})
