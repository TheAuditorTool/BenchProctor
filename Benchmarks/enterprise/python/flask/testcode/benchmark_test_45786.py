# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest45786():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
