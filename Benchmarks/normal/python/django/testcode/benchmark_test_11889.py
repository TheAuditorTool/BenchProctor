# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest11889(request):
    raw_body = request.body.decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JsonResponse({'validated': str(processed)}, status=200)
    return JsonResponse({"saved": True})
