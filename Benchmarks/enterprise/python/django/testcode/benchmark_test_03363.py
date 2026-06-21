# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest03363(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
