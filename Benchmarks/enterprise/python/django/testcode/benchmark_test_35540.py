# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def BenchmarkTest35540(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    digest = hashlib.sha256(str(graphql_var).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return JsonResponse({"saved": True})
