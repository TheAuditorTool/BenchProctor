# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest71373(request):
    env_value = os.environ.get('USER_INPUT', '')
    pending = list(str(env_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
