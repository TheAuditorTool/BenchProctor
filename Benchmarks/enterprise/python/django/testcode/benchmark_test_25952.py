# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest25952(request):
    xml_value = request.body.decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    requests.get(str(data))
    return JsonResponse({"saved": True})
