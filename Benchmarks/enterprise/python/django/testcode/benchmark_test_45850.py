# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest45850(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    reader = make_reader(origin_value)
    data = reader()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
