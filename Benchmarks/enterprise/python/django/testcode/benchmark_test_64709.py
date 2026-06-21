# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64709(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
