# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest51493(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
