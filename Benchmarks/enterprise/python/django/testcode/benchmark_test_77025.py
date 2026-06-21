# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest77025(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
