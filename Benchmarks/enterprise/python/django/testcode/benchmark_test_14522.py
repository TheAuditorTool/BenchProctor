# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import json
import urllib.parse


def to_text(value):
    return str(value).strip()

def BenchmarkTest14522(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
