# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest37836(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
