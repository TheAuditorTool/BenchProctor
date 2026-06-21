# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import importlib
import sys


def BenchmarkTest22804(request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
