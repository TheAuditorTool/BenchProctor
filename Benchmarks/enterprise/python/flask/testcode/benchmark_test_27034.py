# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
import json


def BenchmarkTest27034(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
