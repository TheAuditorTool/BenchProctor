# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import json
from flask import request


def BenchmarkTest42965():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    return redirect(str(data))
