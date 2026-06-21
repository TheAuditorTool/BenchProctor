# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def BenchmarkTest63783(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    if not auth_check(request.session.get('user', ''), str(data)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
