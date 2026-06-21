# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import importlib
import sys


def BenchmarkTest52558(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = full_path
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
