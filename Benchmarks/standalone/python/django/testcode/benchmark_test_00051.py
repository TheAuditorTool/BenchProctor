# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest00051(request):
    raw_body = request.body.decode('utf-8')
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
