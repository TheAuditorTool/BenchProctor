# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest49401(request):
    multipart_value = request.POST.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
