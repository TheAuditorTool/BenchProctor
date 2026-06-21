# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def BenchmarkTest18538(request):
    env_value = os.environ.get('USER_INPUT', '')
    with open('/var/app/data/' + str(env_value), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
