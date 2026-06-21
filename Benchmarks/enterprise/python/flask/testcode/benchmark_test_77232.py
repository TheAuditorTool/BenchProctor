# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest77232():
    xml_value = request.get_data(as_text=True)
    data = '%s' % str(xml_value)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
