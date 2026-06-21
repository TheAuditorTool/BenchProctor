# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest55235(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return JsonResponse({"saved": True})
