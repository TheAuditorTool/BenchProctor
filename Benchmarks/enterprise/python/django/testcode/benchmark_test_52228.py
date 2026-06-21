# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest52228(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
