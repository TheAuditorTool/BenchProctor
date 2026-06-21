# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest28475(request):
    multipart_value = request.POST.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
