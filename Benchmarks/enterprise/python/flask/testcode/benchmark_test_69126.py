# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os


def BenchmarkTest69126():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    return render_template_string(data)
