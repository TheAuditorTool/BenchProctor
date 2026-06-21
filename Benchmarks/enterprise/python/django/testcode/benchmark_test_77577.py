# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import subprocess


def BenchmarkTest77577(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    kind = 'json' if str(graphql_var).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = graphql_var
            data = parsed
        case _:
            data = graphql_var
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
