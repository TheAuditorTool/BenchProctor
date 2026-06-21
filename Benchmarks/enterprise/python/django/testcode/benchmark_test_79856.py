# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import socket


def BenchmarkTest79856(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = str(json_value).replace('\x00', '')
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
