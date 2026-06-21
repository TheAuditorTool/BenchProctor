# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest00988(request, path_param):
    path_value = path_param
    defusedxml.ElementTree.fromstring(str(path_value))
    return JsonResponse({"saved": True})
