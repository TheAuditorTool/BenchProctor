# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest46586(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
