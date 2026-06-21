# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest64698(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
