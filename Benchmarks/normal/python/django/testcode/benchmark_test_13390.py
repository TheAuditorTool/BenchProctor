# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13390(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
