# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest02469(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    return redirect(str(data))
