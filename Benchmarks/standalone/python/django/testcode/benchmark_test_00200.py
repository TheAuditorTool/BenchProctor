# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00200(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
