# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest45495(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
