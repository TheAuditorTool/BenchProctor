# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52856(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
