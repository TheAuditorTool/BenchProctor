# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import sys


def BenchmarkTest73473(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data, _sep, _rest = str(argv_value).partition('\x00')
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
