# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import tempfile


def BenchmarkTest17719(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value:.200s}'
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
