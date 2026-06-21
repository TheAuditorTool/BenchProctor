# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def to_text(value):
    return str(value).strip()

def BenchmarkTest69248(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
