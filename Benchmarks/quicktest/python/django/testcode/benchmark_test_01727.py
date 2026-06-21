# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01727(request):
    host_value = request.META.get('HTTP_HOST', '')
    reader = make_reader(host_value)
    data = reader()
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
