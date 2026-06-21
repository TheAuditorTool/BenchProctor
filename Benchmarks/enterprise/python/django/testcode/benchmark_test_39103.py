# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import os


def BenchmarkTest39103(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
