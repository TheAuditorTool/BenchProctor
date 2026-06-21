# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import importlib
import sys


def BenchmarkTest49942(request):
    cookie_value = request.COOKIES.get('session_token', '')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, cookie_value))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = full_path
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
