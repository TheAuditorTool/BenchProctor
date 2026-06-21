# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import importlib


def BenchmarkTest22750(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value}'
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
