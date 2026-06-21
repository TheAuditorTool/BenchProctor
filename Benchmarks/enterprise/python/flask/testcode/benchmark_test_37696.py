# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest37696():
    xml_value = request.get_data(as_text=True)
    data = '%s' % str(xml_value)
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
