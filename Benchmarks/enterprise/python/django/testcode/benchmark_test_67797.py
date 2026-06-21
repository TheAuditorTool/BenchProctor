# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json


def BenchmarkTest67797(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    with open('/var/app/data/' + str(json_value), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
