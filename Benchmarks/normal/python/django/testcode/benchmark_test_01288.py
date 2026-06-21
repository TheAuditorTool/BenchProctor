# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest01288(request, path_param):
    path_value = path_param
    with open('/var/uploads/' + str(path_value), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
