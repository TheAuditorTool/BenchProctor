# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import re


def BenchmarkTest39113(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
