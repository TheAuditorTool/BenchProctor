# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69925(request, path_param):
    path_value = path_param
    with open('output.csv', 'a') as fh:
        fh.write(str(path_value) + ',data\n')
    return JsonResponse({"saved": True})
