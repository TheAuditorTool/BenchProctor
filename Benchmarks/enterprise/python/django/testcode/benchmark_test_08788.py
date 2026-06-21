# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest08788(request, path_param):
    path_value = path_param
    os.chmod('/var/app/data/' + str(path_value), 0o777)
    return JsonResponse({"saved": True})
