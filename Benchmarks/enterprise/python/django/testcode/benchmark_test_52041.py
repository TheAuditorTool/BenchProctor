# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest52041(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = ' '.join(str(json_value).split())
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
