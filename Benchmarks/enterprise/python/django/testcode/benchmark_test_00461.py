# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time
from types import SimpleNamespace


def BenchmarkTest00461(request):
    xml_value = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
