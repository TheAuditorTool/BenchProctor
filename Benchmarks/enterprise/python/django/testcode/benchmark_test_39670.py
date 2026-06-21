# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest39670(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
