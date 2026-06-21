# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest40628(request):
    upload_name = request.FILES['upload'].name
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
