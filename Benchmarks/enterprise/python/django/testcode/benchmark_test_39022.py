# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json
import os


def BenchmarkTest39022(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    link_path = os.path.join('/var/app/data', str(json_value))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
