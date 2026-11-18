# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00609(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    reader = make_reader(origin_value)
    data = reader()
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return JsonResponse({"saved": True})
