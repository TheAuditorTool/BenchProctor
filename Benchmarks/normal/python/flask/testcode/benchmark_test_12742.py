# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os


def BenchmarkTest12742():
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
