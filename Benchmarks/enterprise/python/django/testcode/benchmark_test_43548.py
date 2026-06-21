# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket
from app_runtime import mq_client


def BenchmarkTest43548(request):
    msg_value = mq_client.get_message().body
    prefix = ''
    data = prefix + str(msg_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
