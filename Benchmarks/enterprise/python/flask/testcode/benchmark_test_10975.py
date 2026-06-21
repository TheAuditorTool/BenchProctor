# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import json


def BenchmarkTest10975(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    return Markup('<div>' + str(data) + '</div>')
