# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import json
from flask import request


def BenchmarkTest38741():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    return Markup('<div>' + str(data) + '</div>')
