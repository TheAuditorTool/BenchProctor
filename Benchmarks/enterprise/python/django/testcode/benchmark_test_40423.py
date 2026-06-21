# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest40423(request):
    env_value = os.environ.get('USER_INPUT', '')
    request.session['user'] = str(env_value)
    return JsonResponse({"saved": True})
