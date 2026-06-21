# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import time
from types import SimpleNamespace
import subprocess


def BenchmarkTest12417(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
