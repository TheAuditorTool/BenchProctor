# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest09054(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
