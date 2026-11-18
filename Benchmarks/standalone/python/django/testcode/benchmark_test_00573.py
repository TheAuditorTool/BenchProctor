# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest00573(request):
    raw_body = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
