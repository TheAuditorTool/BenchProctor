# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
import sys


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest23035(request):
    xml_value = request.body.decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
