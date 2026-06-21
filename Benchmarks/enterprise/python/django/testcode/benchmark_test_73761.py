# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import defusedxml.ElementTree


def BenchmarkTest73761(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
