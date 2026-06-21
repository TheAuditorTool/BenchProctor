# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def coalesce_blank(value):
    return value or ''

def BenchmarkTest77599(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
