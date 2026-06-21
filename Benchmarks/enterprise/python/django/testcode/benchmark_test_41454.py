# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest41454(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
