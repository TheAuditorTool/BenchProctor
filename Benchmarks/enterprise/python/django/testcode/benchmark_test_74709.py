# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def BenchmarkTest74709(request):
    user_id = request.GET.get('id', '')
    sys.path.insert(0, str(user_id))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
