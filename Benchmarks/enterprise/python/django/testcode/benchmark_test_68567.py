# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest68567(request, path_param):
    path_value = path_param
    data = default_blank(path_value)
    if time.time() > 1000000000:
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    return JsonResponse({"saved": True})
