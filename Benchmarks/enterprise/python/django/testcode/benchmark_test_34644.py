# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest34644(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    reader = make_reader(header_value)
    data = reader()
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
