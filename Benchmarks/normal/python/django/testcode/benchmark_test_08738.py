# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import importlib


@dataclass
class FormData:
    payload: str

def BenchmarkTest08738(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
