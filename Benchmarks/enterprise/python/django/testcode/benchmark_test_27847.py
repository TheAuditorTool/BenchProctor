# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import importlib


def BenchmarkTest27847(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
