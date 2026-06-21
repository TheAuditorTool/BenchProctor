# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string


def BenchmarkTest37353(path_param):
    path_value = path_param
    return render_template_string(path_value)
