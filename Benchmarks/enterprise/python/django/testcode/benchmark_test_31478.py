# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest31478(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
