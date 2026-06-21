# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest01825(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
