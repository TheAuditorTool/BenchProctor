# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24502(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
