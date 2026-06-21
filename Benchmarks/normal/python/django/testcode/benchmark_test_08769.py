# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest08769(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
