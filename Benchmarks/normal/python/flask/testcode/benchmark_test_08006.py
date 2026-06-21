# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import os


def BenchmarkTest08006():
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    return redirect(str(data))
