# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect
import os


def BenchmarkTest00136(request):
    env_value = os.environ.get('APP_INPUT', '')
    parts = str(env_value).split(',')
    data = ' '.join(parts)
    return redirect(str(data))
