# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest73738(request):
    host_value = request.META.get('HTTP_HOST', '')
    reader = make_reader(host_value)
    data = reader()
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
