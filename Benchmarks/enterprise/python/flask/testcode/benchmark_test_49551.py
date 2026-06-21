# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import json
from flask import request


def BenchmarkTest49551():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
