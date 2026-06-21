# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
from app_runtime import auth_check


def BenchmarkTest71838(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(graphql_var), store_cred)
    return JsonResponse({"saved": True})
