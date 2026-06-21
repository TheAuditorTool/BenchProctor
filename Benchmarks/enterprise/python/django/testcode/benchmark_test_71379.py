# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import importlib
import sys


def BenchmarkTest71379(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = full_path
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
