# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import time
from types import SimpleNamespace


def BenchmarkTest68873(request):
    raw_body = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    return JsonResponse({"saved": True})
