# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket
import urllib.parse


def BenchmarkTest00081(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    s = socket.create_connection((urllib.parse.urlparse(str(data)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
