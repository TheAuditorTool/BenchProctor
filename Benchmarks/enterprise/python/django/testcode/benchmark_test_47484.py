# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest47484(request):
    user_id = request.GET.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
