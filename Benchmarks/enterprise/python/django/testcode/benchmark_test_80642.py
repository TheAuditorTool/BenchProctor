# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest80642(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    def normalize(value):
        return value.strip()
    data = normalize(graphql_var)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
