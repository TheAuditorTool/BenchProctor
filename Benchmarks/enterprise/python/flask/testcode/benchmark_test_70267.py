# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os


def BenchmarkTest70267():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    return render_template_string(data)
