# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58474():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    eval(str(data))
    return jsonify({"result": "success"})
