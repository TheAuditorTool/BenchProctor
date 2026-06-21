# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest38393(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
