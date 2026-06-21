# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def relay_value(value):
    return value

def BenchmarkTest57070(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
