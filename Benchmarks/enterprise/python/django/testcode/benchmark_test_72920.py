# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest72920(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
