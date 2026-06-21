# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest43370():
    field_value = request.form.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
