# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03308(request, path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
