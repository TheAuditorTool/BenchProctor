# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def BenchmarkTest39880(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
