# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest25476(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
