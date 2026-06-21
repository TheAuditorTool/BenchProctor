# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34669():
    upload_name = request.files['upload'].filename
    kind = 'json' if str(upload_name).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = upload_name
            data = parsed
        case _:
            data = upload_name
    eval(str(data))
    return jsonify({"result": "success"})
