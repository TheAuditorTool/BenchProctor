# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def coalesce_blank(value):
    return value or ''

def BenchmarkTest45679(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    def _primary():
        eval(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
