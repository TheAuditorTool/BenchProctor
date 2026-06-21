# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
import sys


def BenchmarkTest01544(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    if argv_value:
        data = argv_value
    else:
        data = ''
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
