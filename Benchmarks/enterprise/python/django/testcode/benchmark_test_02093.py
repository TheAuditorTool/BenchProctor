# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import re


def BenchmarkTest02093(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    if re.search('[a-zA-Z0-9_-]+', str(graphql_var)):
        return JsonResponse({'validated': str(graphql_var)}, status=200)
    return JsonResponse({"saved": True})
