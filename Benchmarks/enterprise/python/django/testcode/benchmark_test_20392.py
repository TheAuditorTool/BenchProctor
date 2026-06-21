# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
from django.http import HttpResponse


def BenchmarkTest20392(request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
