# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest26188(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
