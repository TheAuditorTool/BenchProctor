# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import json
from types import SimpleNamespace


def BenchmarkTest58380(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
