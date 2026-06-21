# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from django.shortcuts import redirect
import json
import urllib.parse


@dataclass
class FormData:
    payload: str

def BenchmarkTest76539(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
