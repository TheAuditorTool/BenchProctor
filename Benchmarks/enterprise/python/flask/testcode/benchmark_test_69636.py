# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import json
from flask import request


def BenchmarkTest69636():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    return render_template_string(data)
