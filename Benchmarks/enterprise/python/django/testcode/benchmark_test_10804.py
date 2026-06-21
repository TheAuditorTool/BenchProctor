# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json
import time


def relay_value(value):
    return value

def BenchmarkTest10804(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    if time.time() > 1000000000:
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    return JsonResponse({"saved": True})
