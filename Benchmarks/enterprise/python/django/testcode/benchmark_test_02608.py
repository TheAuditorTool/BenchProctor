# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest02608(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
