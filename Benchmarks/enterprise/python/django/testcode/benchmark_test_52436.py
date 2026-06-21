# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest52436(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
