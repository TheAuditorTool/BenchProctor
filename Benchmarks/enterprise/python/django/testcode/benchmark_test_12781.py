# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest12781(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
