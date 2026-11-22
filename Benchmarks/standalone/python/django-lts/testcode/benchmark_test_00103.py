# SPDX-License-Identifier: Apache-2.0
from django.shortcuts import redirect
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00103(request):
    env_value = os.environ.get('APP_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    return redirect(str(data))
