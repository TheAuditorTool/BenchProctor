# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest07298(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    return JsonResponse({'error': str(graphql_var), 'stack': repr(locals())}, status=500)
