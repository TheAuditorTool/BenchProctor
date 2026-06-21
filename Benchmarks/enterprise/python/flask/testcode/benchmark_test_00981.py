# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00981():
    xml_value = request.get_data(as_text=True)
    kind = 'json' if str(xml_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = xml_value
            data = parsed
        case _:
            data = xml_value
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
