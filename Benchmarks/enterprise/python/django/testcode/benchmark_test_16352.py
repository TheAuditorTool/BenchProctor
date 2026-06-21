# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest16352(request):
    upload_name = request.FILES['upload'].name
    reader = make_reader(upload_name)
    data = reader()
    json.loads(data)
    return JsonResponse({"saved": True})
