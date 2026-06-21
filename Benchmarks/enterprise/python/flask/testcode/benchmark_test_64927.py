# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string


def BenchmarkTest64927(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    return render_template_string(data)
