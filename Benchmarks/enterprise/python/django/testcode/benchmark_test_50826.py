# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest50826(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
