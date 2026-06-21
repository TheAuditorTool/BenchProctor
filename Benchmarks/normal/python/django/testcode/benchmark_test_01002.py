# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest01002(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    processed = 'true' if str(graphql_var).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return JsonResponse({"saved": True})
