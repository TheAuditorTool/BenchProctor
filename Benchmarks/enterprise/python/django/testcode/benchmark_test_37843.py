# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import defusedxml.ElementTree


def BenchmarkTest37843(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    defusedxml.ElementTree.fromstring(str(graphql_var))
    return JsonResponse({"saved": True})
