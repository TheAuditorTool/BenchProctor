# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest25631():
    xml_value = request.get_data(as_text=True)
    data, _sep, _rest = str(xml_value).partition('\x00')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
