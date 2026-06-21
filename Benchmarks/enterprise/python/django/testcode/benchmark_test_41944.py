# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest41944(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    request.session['data'] = str(graphql_var)
    return JsonResponse({"saved": True})
