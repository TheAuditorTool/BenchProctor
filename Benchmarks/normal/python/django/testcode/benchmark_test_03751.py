# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest03751(request, path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
