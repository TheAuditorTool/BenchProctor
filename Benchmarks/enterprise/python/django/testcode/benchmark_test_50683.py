# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import importlib
import sys


def BenchmarkTest50683(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
