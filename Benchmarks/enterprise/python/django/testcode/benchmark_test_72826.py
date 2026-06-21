# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse
import json


def BenchmarkTest72826(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
