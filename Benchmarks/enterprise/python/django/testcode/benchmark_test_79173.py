# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def ensure_str(value):
    return str(value)

def BenchmarkTest79173(request):
    stdin_value = input('input: ')
    data = ensure_str(stdin_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
