# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
from types import SimpleNamespace


def BenchmarkTest33254(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
