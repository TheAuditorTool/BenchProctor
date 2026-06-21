# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest12532(request):
    user_id = request.GET.get('id', '')
    pending = list(str(user_id).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
