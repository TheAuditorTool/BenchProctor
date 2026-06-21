# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os


def BenchmarkTest03092():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    return render_template_string(data)
