# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest11982(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
