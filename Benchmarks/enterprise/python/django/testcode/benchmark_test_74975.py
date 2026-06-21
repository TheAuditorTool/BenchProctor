# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest74975(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
