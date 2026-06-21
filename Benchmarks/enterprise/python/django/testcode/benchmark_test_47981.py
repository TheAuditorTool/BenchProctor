# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
import json


def BenchmarkTest47981(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(graphql_var)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = graphql_var
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
