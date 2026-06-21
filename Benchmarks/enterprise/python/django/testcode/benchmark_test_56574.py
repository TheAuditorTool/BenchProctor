# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json


request_state: dict[str, str] = {}

def BenchmarkTest56574(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
