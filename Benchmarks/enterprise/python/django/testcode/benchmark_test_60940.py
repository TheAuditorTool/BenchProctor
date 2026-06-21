# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import socket


def relay_value(value):
    return value

def BenchmarkTest60940(request):
    user_id = request.GET.get('id', '')
    data = relay_value(user_id)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
