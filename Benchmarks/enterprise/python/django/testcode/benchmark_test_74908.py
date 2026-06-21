# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json


def BenchmarkTest74908(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
