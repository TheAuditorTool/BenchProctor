# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24809():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
