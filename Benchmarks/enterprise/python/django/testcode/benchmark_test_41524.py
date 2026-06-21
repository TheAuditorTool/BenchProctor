# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest41524(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    reader = make_reader(ua_value)
    data = reader()
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
