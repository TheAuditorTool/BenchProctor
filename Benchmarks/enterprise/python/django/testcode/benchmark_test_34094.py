# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest34094(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
