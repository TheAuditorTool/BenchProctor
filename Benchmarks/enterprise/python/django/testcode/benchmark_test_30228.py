# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest30228(request):
    user_id = request.GET.get('id', '')
    parts = []
    for token in str(user_id).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
