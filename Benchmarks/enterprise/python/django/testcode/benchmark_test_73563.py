# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def ensure_str(value):
    return str(value)

def BenchmarkTest73563(request, path_param):
    path_value = path_param
    data = ensure_str(path_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
