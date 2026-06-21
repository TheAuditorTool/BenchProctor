# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def BenchmarkTest29131(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    return HttpResponse(str(data), content_type='text/html')
