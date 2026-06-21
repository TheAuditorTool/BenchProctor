# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest03826(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
