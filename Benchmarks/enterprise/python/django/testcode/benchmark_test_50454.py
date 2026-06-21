# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
import sys


def BenchmarkTest50454(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data, _sep, _rest = str(argv_value).partition('\x00')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
