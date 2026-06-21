# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from types import SimpleNamespace


def BenchmarkTest23908(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
