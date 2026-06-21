# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os


def BenchmarkTest52509():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    return render_template_string(data)
