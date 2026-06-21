# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest25740(request):
    multipart_value = request.POST.get('multipart_field', '')
    pending = list(str(multipart_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
