# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import importlib
import sys


def BenchmarkTest25075(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
