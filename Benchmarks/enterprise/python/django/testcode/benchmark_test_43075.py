# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def BenchmarkTest43075(request):
    env_value = os.environ.get('USER_INPUT', '')
    return HttpResponse('<!-- diagnostic build token: ' + str(env_value) + ' -->', content_type='text/html')
