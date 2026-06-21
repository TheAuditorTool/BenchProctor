# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from types import SimpleNamespace


def BenchmarkTest17895(request):
    upload_name = request.FILES['upload'].name
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    processed = data[:64]
    globals()['counter'] = int(processed)
    return JsonResponse({"saved": True})
