# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def relay_value(value):
    return value

def BenchmarkTest03760(request, path_param):
    path_value = path_param
    data = relay_value(path_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
