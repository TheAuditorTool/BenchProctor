# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import json


def BenchmarkTest77465():
    origin_value = request.headers.get('Origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    return Markup('<img src="' + str(data) + '">')
