# SPDX-License-Identifier: Apache-2.0
import json


def BenchmarkTest79701(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
