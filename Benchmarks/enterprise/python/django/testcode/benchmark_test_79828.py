# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest79828(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
