# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest12663(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
