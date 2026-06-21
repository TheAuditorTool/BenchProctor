# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import importlib


@dataclass
class FormData:
    payload: str

def BenchmarkTest67789(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
