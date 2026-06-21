# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08824(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
