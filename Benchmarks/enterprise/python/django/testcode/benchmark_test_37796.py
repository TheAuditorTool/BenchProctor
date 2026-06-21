# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest37796(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    os.remove(str(data))
    return JsonResponse({"saved": True})
