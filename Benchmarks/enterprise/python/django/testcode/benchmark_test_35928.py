# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
from django.http import HttpResponse


def BenchmarkTest35928(request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
