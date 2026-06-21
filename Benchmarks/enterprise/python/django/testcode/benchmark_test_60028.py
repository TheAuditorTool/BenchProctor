# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import json


request_state: dict[str, str] = {}

def BenchmarkTest60028(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
