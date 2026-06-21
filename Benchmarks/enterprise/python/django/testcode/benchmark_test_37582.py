# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest37582(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
