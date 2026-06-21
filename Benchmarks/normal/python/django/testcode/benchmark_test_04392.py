# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest04392(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
