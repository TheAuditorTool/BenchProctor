# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest01430(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
