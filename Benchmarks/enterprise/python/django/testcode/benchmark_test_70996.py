# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest70996(request):
    multipart_value = request.POST.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
