# SPDX-License-Identifier: Apache-2.0
import os
from flask import redirect
import urllib.parse


def BenchmarkTest52506():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
