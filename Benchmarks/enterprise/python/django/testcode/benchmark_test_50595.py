# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
from types import SimpleNamespace


def BenchmarkTest50595(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
