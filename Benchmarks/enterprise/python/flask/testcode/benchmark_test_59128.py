# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import os


def BenchmarkTest59128():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    return redirect(str(data))
