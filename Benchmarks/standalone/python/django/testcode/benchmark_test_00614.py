# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest00614(request):
    field_value = request.POST.get('field', '')
    data = '%s' % str(field_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
