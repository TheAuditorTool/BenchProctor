# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import sys


def BenchmarkTest01812(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    if argv_value:
        data = argv_value
    else:
        data = ''
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
