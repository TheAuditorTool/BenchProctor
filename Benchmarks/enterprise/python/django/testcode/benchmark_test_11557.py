# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest11557(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
