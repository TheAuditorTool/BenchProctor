# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest00285(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ' '.join(parts)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
