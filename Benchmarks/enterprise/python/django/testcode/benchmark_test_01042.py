# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import json
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest01042(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
