# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def BenchmarkTest50657(request):
    upload_name = request.FILES['upload'].name
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
