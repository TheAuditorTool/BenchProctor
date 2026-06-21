# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def BenchmarkTest37302(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    auth_check('user', graphql_var)
    return JsonResponse({"saved": True})
