# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest32485():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    os.remove(str(data))
    return jsonify({"result": "success"})
