# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37534(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
