# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest00137(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
