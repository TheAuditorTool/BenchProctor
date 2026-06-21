# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import importlib


def normalise_input(value):
    return value.strip()

def BenchmarkTest09966(request):
    raw_body = request.body.decode('utf-8')
    data = normalise_input(raw_body)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
