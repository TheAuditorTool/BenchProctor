# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest06612(request):
    env_value = os.environ.get('USER_INPUT', '')
    with open('/var/uploads/' + str(env_value), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
