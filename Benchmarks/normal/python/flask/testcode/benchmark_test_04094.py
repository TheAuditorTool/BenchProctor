# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os


def BenchmarkTest04094():
    env_value = os.environ.get('USER_INPUT', '')
    return render_template_string(env_value)
