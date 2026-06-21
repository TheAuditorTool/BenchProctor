# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest54327(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
