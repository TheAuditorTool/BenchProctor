# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest65423(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    subprocess.run([str(auth_header), '--status'], shell=False)
    return JsonResponse({"saved": True})
