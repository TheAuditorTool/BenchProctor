# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest22996(request):
    upload_name = request.FILES['upload'].name
    ctx = RequestContext(upload_name)
    data = ctx.payload
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
