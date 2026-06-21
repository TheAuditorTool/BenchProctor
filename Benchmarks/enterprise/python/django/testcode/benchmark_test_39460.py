# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest39460(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
