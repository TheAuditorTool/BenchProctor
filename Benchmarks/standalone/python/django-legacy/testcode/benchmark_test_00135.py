# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00135(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    reader = make_reader(origin_value)
    data = reader()
    return redirect(str(data))
