# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest06672(request):
    stdin_value = input('input: ')
    def normalize(value):
        return value.strip()
    data = normalize(stdin_value)
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
