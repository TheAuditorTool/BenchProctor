# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def BenchmarkTest36954(request):
    upload_name = request.FILES['upload'].name
    processed = shlex.quote(upload_name)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
