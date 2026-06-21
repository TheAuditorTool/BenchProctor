# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from django.http import HttpResponse


def BenchmarkTest04187(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = json.loads(json_value).get('value', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
