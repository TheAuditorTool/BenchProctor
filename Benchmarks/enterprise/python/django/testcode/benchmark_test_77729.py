# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest77729(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
