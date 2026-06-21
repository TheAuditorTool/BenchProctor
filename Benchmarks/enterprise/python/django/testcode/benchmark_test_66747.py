# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from django.http import HttpResponse


def BenchmarkTest66747(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
