# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03807(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
