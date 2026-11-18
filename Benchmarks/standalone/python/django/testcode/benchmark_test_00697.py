# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect
import os


def BenchmarkTest00697(request):
    env_value = os.environ.get('APP_INPUT', '')
    return redirect(str(env_value))
