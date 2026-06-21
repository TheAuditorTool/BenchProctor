# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
import subprocess


def BenchmarkTest38669(request):
    multipart_value = request.POST.get('multipart_field', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', multipart_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = multipart_value
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
