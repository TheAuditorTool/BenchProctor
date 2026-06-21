# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import os


def BenchmarkTest12005():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    return redirect(str(data))
