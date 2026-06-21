# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
from types import SimpleNamespace
import subprocess


def BenchmarkTest07647(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    def _primary():
        subprocess.run([str(data), '--status'], shell=False)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
