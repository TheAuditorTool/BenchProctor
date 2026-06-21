# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest31916(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
