# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest14586(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    reader = make_reader(header_value)
    data = reader()
    return redirect(str(data))
