# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest75225(request):
    xml_value = request.body.decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
