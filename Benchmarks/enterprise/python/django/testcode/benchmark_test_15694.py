# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace
import defusedxml.ElementTree


def BenchmarkTest15694(request):
    raw_body = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
