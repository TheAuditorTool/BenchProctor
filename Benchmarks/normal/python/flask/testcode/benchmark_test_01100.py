# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os


def BenchmarkTest01100():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    return render_template_string('safe block: {{ value }}', value=data)
