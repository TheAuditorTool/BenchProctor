# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import socket
from app_runtime import mq_client


def coalesce_blank(value):
    return value or ''

def BenchmarkTest23461(request):
    msg_value = mq_client.get_message().body
    data = coalesce_blank(msg_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
