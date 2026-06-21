# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import sys


def BenchmarkTest26354(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = (lambda v: v.strip())(argv_value)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
