# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest11508(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    trusted_claim = str(graphql_var)
    return JsonResponse({'trusted': trusted_claim}, status=200)
