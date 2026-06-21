# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import socket
from app_runtime import mq_client


def to_text(value):
    return str(value).strip()

def BenchmarkTest00140(request):
    msg_value = mq_client.get_message().body
    data = to_text(msg_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
