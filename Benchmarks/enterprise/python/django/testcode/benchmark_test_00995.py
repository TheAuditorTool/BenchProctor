# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00995(request):
    raw_body = request.body.decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
