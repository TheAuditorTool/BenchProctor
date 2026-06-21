# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest75385(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    reader = make_reader(referer_value)
    data = reader()
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
