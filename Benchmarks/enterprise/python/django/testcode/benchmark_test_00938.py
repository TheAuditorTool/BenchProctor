# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import re
import json


def to_text(value):
    return str(value).strip()

def BenchmarkTest00938(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
