# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest68468(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
