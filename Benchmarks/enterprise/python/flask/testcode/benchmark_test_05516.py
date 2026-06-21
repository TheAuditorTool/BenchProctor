# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import json
import urllib.parse


def BenchmarkTest05516():
    field_value = request.form.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
