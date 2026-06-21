# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import html
from types import SimpleNamespace


def BenchmarkTest12904(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    processed = str(data).replace("<script", "")
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return JsonResponse({"saved": True})
