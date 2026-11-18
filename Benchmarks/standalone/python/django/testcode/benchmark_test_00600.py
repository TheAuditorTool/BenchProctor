# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00600(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    eval(str(data))
    return JsonResponse({"saved": True})
