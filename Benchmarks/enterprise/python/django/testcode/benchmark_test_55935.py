# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import importlib
import sys


def BenchmarkTest55935(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
