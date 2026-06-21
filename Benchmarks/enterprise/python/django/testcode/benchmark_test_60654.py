# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest60654(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
