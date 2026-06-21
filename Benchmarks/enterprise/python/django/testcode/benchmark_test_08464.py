# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest08464(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(graphql_var))
    return JsonResponse({'lookup': arr[idx]}, status=200)
