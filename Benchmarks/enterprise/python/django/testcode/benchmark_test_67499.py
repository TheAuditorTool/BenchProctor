# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67499(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
