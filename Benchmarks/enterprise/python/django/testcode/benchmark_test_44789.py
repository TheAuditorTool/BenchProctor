# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass
import importlib
import sys


@dataclass
class FormData:
    payload: str

def BenchmarkTest44789(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = full_path
    sys.path.insert(0, '/opt/app/plugins')
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
