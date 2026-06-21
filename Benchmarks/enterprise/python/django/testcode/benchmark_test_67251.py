# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest67251(request):
    upload_name = request.FILES['upload'].name
    reader = make_reader(upload_name)
    data = reader()
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
