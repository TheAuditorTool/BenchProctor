# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest07829(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
