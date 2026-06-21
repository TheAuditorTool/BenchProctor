# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest12201(request):
    upload_name = request.FILES['upload'].name
    subprocess.run([str(upload_name), '--status'], shell=False)
    return JsonResponse({"saved": True})
