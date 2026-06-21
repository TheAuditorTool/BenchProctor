# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest78559(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
