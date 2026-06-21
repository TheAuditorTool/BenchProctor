# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest30621(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    subprocess.run([str(header_value), '--status'], shell=False)
    return JsonResponse({"saved": True})
