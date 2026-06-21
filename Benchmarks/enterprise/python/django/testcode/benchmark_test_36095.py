# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest36095(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    defusedxml.ElementTree.fromstring(str(ua_value))
    return JsonResponse({"saved": True})
