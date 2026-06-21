# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76727(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
