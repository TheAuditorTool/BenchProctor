# SPDX-License-Identifier: Apache-2.0
import os
from flask import redirect
import urllib.parse


def BenchmarkTest35837():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
