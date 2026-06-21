# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
from types import SimpleNamespace


def BenchmarkTest12726(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return JsonResponse({"saved": True})
