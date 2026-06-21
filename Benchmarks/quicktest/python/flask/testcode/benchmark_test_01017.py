# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os


def BenchmarkTest01017():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    return render_template_string(data)
