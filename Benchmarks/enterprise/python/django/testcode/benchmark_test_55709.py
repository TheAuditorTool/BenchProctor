# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest55709(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '%s' % (header_value,)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
