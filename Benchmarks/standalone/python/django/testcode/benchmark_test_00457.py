# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import socket


def BenchmarkTest00457(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
