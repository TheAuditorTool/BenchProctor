# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import importlib


def BenchmarkTest00420(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
