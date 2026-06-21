# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30046(request, path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
