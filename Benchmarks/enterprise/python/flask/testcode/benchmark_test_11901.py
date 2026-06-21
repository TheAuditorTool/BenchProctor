# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11901():
    xml_value = request.get_data(as_text=True)
    kind = 'json' if str(xml_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = xml_value
            data = parsed
        case _:
            data = xml_value
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
