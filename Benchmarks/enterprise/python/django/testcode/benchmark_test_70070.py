# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


def BenchmarkTest70070(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
