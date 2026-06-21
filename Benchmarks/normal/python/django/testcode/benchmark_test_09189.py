# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest09189(request):
    env_value = os.environ.get('USER_INPUT', '')
    os.chmod('/var/app/data/' + str(env_value), 0o777)
    return JsonResponse({"saved": True})
