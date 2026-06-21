# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest71132(request):
    raw_body = request.body.decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    return redirect(str(data))
