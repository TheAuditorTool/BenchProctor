# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from urllib.parse import unquote


def BenchmarkTest19672(path_param):
    path_value = path_param
    data = unquote(path_value)
    return render_template_string(data)
