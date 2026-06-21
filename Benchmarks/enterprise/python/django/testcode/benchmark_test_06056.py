# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest06056(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
