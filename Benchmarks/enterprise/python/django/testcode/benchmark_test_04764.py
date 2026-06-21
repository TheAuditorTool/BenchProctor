# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import socket


def BenchmarkTest04764(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    s = socket.create_connection((str(graphql_var), 80))
    s.close()
    return JsonResponse({"saved": True})
