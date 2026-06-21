# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os


def BenchmarkTest78235():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    return render_template_string(data)
