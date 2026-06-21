# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest04897():
    xml_value = request.get_data(as_text=True)
    data, _sep, _rest = str(xml_value).partition('\x00')
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
