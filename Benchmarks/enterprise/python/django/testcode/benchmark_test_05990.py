# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest05990(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
