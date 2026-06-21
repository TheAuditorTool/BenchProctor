# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket
from app_runtime import mq_client


def BenchmarkTest30453(request):
    msg_value = mq_client.get_message().body
    data = msg_value.decode('utf-8', 'ignore') if isinstance(msg_value, bytes) else msg_value
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
