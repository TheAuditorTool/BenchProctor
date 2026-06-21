# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def relay_value(value):
    return value

def BenchmarkTest21934(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return HttpResponse(content)
    return JsonResponse({"saved": True})
