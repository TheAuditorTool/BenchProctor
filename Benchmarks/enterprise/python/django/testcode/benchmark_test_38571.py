# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest38571(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
