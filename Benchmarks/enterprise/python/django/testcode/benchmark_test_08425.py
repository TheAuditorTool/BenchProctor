# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest08425(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
