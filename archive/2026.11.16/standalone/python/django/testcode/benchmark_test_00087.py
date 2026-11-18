# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00087(request):
    field_value = request.POST.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    eval(str(data))
    return JsonResponse({"saved": True})
