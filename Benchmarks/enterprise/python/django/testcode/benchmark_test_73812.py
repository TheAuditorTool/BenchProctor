# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest73812(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
