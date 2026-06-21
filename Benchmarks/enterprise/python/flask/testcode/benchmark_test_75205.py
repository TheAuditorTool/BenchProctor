# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import json


def BenchmarkTest75205(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    return render_template_string(data)
