# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.core.cache import cache
import json


def BenchmarkTest00092(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    cache.set('active_tenant', str(data), None)
    return JsonResponse({"saved": True})
