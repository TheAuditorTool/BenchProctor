# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest12030(request):
    xml_value = request.body.decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
