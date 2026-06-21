# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def BenchmarkTest42410(request):
    stdin_value = input('input: ')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(stdin_value)
    data = collected
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
