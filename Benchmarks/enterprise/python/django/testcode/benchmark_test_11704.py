# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest11704(request):
    multipart_value = request.POST.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    return redirect(str(data))
