# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest16982(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
