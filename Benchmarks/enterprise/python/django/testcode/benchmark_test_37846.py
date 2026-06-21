# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest37846(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
