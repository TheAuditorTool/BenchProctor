# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import json
from types import SimpleNamespace


def BenchmarkTest30262(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
