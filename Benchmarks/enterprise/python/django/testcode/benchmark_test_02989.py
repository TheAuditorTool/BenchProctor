# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
import json
from types import SimpleNamespace


def BenchmarkTest02989(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s./\\\\:_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('/var/uploads/' + str(processed), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
