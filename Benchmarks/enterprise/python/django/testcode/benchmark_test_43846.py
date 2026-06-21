# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest43846(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % (host_value,)
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
