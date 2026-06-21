# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest05509(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(graphql_var))
    return resp
