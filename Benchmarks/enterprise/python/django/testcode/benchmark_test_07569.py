# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest07569(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    os.remove(str(data))
    return JsonResponse({"saved": True})
