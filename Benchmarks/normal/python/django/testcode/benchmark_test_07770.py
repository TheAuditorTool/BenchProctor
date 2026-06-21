# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import socket


def BenchmarkTest07770(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
