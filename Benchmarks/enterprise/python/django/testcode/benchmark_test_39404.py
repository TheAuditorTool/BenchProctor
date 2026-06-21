# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest39404(request):
    user_id = request.GET.get('id', '')
    if user_id not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = user_id
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
