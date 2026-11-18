# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import ctypes


def BenchmarkTest00207(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
