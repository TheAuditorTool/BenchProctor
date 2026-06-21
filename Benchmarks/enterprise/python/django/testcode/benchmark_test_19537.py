# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import sys


def BenchmarkTest19537(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    def normalize(value):
        return value.strip()
    data = normalize(argv_value)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
