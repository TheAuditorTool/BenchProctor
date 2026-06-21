# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest26078(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return JsonResponse({'error': 'privilege drop failed'}, status=500)
    return JsonResponse({"saved": True})
