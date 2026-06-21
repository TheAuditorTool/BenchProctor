# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
import json


request_state: dict[str, str] = {}

def BenchmarkTest31173(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    requests.get(str(data))
    return JsonResponse({"saved": True})
