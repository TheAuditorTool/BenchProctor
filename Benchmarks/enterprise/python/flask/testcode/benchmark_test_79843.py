# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest79843():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value}'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
