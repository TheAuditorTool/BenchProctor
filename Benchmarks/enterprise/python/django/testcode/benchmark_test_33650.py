# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest33650(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
