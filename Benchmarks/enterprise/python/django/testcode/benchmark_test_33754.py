# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import json


request_state: dict[str, str] = {}

def BenchmarkTest33754(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    processed = data[:64]
    return redirect(str(processed))
