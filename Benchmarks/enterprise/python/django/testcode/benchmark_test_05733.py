# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import sys


def BenchmarkTest05733(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    subprocess.Popen('echo ' + str(argv_value), shell=True).wait()
    return JsonResponse({"saved": True})
