# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest35082():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    session['data'] = str(data)
    return jsonify({"result": "success"})
