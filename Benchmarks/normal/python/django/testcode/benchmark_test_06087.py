# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import os


def BenchmarkTest06087(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    return redirect(str(data))
