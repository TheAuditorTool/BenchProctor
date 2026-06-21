# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00286(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
