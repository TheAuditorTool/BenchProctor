# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def BenchmarkTest81321(request):
    multipart_value = request.POST.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
