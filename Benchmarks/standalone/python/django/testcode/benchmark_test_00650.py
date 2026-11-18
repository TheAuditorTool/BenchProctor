# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00650(request):
    raw_body = request.body.decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    exec(str(processed))
    return JsonResponse({"saved": True})
