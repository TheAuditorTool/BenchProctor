# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest70341(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
