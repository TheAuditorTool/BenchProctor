# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest01817(request, path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    os.seteuid(65534)
    return JsonResponse({"saved": True})
