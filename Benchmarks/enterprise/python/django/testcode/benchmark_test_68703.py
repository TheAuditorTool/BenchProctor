# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest68703(request):
    multipart_value = request.POST.get('multipart_field', '')
    subprocess.run([str(multipart_value), '--status'], shell=False)
    return JsonResponse({"saved": True})
