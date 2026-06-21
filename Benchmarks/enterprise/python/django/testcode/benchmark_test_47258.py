# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import socket


def BenchmarkTest47258(request):
    user_id = request.GET.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
