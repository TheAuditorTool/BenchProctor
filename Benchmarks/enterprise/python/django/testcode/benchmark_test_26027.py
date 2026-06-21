# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest26027(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = default_blank(host_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
