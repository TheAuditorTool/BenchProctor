# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest27224(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
