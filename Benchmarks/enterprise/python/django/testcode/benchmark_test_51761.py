# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import importlib
import sys


@dataclass
class FormData:
    payload: str

def BenchmarkTest51761(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
