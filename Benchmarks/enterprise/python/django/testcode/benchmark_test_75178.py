# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest75178(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
