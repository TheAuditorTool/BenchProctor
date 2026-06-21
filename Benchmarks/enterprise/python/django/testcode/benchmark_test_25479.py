# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import ctypes


def ensure_str(value):
    return str(value)

def BenchmarkTest25479(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
