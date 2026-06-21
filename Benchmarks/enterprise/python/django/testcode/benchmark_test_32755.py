# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace
import defusedxml.ElementTree


def BenchmarkTest32755(request):
    upload_name = request.FILES['upload'].name
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
