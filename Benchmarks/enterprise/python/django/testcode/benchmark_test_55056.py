# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest55056(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
