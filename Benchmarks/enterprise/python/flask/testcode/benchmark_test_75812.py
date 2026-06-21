# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest75812():
    xml_value = request.get_data(as_text=True)
    data = '%s' % str(xml_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
