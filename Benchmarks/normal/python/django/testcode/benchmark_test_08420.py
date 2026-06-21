# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest08420(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(processed)})
