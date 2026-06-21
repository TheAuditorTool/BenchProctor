# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import socket


def BenchmarkTest15048(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value:.200s}'
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
