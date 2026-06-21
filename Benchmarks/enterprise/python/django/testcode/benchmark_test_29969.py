# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest29969(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
