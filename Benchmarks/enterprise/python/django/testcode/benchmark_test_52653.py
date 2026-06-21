# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest52653(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
