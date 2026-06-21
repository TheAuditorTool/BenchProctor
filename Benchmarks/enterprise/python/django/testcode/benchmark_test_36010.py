# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest36010(request):
    stdin_value = input('input: ')
    def normalize(value):
        return value.strip()
    data = normalize(stdin_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return JsonResponse({"saved": True})
