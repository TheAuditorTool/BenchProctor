# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import os


def BenchmarkTest03640():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    return redirect(str(data))
