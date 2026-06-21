# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import importlib
import sys


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest11357(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
