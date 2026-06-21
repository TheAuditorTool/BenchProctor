# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import importlib


def BenchmarkTest53139(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
