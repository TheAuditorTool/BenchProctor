# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import importlib
import sys


def BenchmarkTest41682(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, header_value))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = full_path
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
