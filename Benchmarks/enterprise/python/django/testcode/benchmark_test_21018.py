# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest21018(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    os.remove(str(graphql_var))
    return JsonResponse({"saved": True})
