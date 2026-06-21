# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse
import json


def normalise_input(value):
    return value.strip()

def BenchmarkTest67866(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = normalise_input(json_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
