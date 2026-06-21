# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from types import SimpleNamespace


def BenchmarkTest15055(request):
    upload_name = request.FILES['upload'].name
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    os.remove(str(data))
    return JsonResponse({"saved": True})
