# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest35854(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
