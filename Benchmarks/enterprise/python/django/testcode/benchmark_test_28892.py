# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import socket


@dataclass
class FormData:
    payload: str

def BenchmarkTest28892(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
