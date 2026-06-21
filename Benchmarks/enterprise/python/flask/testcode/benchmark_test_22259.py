# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest22259():
    xml_value = request.get_data(as_text=True)
    session['data'] = str(xml_value)
    return jsonify({"result": "success"})
