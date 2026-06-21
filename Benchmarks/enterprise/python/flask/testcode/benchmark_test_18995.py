# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string


def BenchmarkTest18995(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    return render_template_string(data)
