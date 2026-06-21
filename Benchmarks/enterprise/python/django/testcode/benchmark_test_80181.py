# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import ctypes


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest80181(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
