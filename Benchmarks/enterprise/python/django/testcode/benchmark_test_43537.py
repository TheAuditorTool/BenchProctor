# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43537(request, path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
