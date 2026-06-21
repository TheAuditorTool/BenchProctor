# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import os


def BenchmarkTest05676():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    return redirect(str(data))
