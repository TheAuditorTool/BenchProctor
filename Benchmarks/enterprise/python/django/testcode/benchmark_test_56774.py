# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest56774(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
