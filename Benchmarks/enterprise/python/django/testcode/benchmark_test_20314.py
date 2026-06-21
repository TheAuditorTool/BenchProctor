# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest20314(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
