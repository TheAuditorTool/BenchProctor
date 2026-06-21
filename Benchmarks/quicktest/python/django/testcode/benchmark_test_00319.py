# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse
import json


def coalesce_blank(value):
    return value or ''

def BenchmarkTest00319(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
