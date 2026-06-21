# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest34225(request):
    upload_name = request.FILES['upload'].name
    reader = make_reader(upload_name)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
