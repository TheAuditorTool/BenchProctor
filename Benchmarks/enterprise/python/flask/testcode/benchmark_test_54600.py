# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54600():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    exec(str(data))
    return jsonify({"result": "success"})
