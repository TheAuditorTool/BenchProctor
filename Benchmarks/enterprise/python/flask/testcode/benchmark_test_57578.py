# SPDX-License-Identifier: Apache-2.0
import os
from flask import redirect
import urllib.parse


def BenchmarkTest57578():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
