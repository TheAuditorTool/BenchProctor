# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66185(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
