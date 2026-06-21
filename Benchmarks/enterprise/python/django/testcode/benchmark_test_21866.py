# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest21866(request):
    raw_body = request.body.decode('utf-8')
    data = '{}'.format(raw_body)
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
