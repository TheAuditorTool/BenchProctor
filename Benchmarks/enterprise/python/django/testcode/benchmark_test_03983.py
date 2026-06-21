# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest03983(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '{}'.format(auth_header)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
