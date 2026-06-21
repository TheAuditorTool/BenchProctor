# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
from types import SimpleNamespace


def BenchmarkTest00595(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    eval(compile("os.system('echo ' + str(data))", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
