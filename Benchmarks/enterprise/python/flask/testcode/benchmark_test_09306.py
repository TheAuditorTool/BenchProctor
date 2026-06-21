# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest09306():
    xml_value = request.get_data(as_text=True)
    os.chmod('/var/app/data/' + str(xml_value), 0o777)
    return jsonify({"result": "success"})
