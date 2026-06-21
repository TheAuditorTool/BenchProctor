# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70482(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
