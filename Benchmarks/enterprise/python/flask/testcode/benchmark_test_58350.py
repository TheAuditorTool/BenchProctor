# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest58350():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
