# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import defusedxml.ElementTree


def BenchmarkTest11171(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
