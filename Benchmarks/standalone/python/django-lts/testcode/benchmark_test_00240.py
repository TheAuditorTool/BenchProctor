# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from pathlib import Path


def BenchmarkTest00240(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    parts = []
    for token in str(graphql_var).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    Path('/var/app/data/' + str(data)).write_text('data')
    return JsonResponse({"saved": True})
