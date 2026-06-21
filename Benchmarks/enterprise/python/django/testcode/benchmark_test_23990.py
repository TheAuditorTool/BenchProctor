# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23990(request, path_param):
    path_value = path_param
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(path_value))
    return JsonResponse({"saved": True})
