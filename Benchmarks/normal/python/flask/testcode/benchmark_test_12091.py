# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest12091():
    xml_value = request.get_data(as_text=True)
    globals()['counter'] = int(xml_value)
    return jsonify({"result": "success"})
