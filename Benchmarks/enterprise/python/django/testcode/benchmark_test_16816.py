# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
from django.http import HttpResponse


def BenchmarkTest16816(request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
