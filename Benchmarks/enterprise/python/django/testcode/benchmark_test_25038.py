# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25038(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
