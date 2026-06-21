# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def coalesce_blank(value):
    return value or ''

def BenchmarkTest26803(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
