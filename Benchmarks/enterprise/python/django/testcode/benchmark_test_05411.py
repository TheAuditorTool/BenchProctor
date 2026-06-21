# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest05411(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
