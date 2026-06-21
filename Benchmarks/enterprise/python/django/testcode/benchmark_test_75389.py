# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest75389(request):
    upload_name = request.FILES['upload'].name
    reader = make_reader(upload_name)
    data = reader()
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
