# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import json
import urllib.parse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest33278(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = handle(graphql_var)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
