# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import tempfile


def BenchmarkTest48782(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(json_value))
    return JsonResponse({"saved": True})
