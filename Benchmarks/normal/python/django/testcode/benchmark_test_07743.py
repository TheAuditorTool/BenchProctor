# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
from django.http import HttpResponse


def BenchmarkTest07743(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = json.loads(json_value).get('value', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
