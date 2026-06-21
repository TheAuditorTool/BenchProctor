# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace
import defusedxml.ElementTree


def BenchmarkTest72899(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
