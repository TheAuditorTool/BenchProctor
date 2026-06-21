# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def normalise_input(value):
    return value.strip()

def BenchmarkTest19644(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return JsonResponse({"saved": True})
