# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest30388(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
