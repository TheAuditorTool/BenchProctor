# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest77994(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
