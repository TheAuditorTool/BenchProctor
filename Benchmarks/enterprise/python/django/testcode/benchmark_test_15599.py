# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
import sys


def BenchmarkTest15599(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    def normalize(value):
        return value.strip()
    data = normalize(argv_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
