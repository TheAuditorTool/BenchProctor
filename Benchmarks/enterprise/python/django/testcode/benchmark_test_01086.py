# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json


def BenchmarkTest01086(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
