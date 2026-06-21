# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest13007(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
