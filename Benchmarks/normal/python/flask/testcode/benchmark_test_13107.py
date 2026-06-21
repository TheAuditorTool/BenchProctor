# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def BenchmarkTest13107():
    field_value = request.form.get('field', '')
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = field_value
            data = parsed
        case _:
            data = field_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
