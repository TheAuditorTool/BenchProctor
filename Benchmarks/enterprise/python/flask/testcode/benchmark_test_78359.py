# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78359():
    xml_value = request.get_data(as_text=True)
    kind = 'json' if str(xml_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = xml_value
            data = parsed
        case _:
            data = xml_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
