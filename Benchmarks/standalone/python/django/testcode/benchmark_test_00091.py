# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket
import urllib.parse


def BenchmarkTest00091(request, path_param):
    path_value = path_param
    pending = list(str(path_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    s = socket.create_connection((urllib.parse.urlparse(str(data)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
