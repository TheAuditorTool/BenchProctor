# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest21344(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    int(str(data))
    return JsonResponse({"saved": True})
