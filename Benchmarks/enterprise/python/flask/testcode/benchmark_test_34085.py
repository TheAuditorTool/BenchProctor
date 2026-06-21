# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import json


def BenchmarkTest34085():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    return Markup('<div>' + str(data) + '</div>')
