# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import importlib
import sys


def BenchmarkTest61404(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    sys.path.insert(0, str(graphql_var))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
