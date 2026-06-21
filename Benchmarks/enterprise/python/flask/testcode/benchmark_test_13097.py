# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os


def BenchmarkTest13097():
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    return render_template_string('safe block: {{ value }}', value=data)
