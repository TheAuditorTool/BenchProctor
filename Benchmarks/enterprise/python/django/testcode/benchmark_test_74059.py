# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


request_state: dict[str, str] = {}

def BenchmarkTest74059(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
