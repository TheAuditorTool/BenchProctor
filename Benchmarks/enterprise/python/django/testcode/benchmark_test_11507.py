# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import re


request_state: dict[str, str] = {}

def BenchmarkTest11507(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
