# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00082(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = ' '.join(str(env_value).split())
    exec(str(data))
    return JsonResponse({"saved": True})
