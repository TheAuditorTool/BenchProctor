# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01179(request):
    xml_value = request.body.decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
