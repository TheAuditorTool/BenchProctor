# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
from types import SimpleNamespace


def BenchmarkTest25754(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return JsonResponse({"saved": True})
