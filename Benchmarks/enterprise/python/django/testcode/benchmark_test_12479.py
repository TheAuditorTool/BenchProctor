# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import json
import urllib.parse


def BenchmarkTest12479(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    parts = []
    for token in str(json_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
