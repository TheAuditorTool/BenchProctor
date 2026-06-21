# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string


def BenchmarkTest63756(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    return render_template_string(data)
