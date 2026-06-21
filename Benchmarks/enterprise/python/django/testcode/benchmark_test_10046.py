# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest10046(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
