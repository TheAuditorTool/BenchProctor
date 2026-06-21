# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest09008(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
