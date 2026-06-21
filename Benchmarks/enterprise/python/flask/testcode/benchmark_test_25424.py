# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import markdown
import bleach
import json
from flask import request


def BenchmarkTest25424():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    processed = bleach.clean(markdown.markdown(data))
    return Markup('<div>' + str(processed) + '</div>')
