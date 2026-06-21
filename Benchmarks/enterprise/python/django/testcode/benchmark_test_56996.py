# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
import json
from types import SimpleNamespace


def BenchmarkTest56996(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
