# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest78270(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % (host_value,)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
