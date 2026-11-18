# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import re


def BenchmarkTest00525(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    pending = list(str(graphql_var).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    exec(str(processed))
    return JsonResponse({"saved": True})
