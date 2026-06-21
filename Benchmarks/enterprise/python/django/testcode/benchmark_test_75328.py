# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest75328(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
