# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from types import SimpleNamespace


def BenchmarkTest20499(request):
    xml_value = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
