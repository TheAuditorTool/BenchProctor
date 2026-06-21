# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string


def BenchmarkTest33000(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    return render_template_string(data)
