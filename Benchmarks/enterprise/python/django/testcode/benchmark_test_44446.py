# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json
import os


def relay_value(value):
    return value

def BenchmarkTest44446(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return HttpResponse(content)
    return JsonResponse({"saved": True})
