# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os


def BenchmarkTest66394():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    return render_template_string(data)
