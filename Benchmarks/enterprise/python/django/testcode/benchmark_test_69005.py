# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69005(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
