# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def BenchmarkTest78372(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    return HttpResponse(str(data), content_type='text/html')
