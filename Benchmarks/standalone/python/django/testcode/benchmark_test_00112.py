# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


def BenchmarkTest00112(request, path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
