# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import sys


def BenchmarkTest02846(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = ' '.join(str(argv_value).split())
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
