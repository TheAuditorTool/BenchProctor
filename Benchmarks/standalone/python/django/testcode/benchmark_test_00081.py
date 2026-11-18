# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest00081(request):
    field_value = request.POST.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
